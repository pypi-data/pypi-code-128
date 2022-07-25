"""A module for the websockets-based Client for Jina."""
import asyncio
from contextlib import AsyncExitStack
from typing import TYPE_CHECKING, Dict, Optional, Tuple

from starlette import status

from jina.clients.base import BaseClient
from jina.clients.base.helper import WebsocketClientlet
from jina.clients.helper import callback_exec
from jina.helper import get_or_reuse_loop
from jina.importer import ImportExtensions
from jina.logging.profile import ProgressBar
from jina.proto import jina_pb2
from jina.serve.stream import RequestStreamer

if TYPE_CHECKING:
    from jina.clients.base import CallbackFnType, InputType
    from jina.types.request import Request


class WebSocketBaseClient(BaseClient):
    """A Websocket Client."""

    async def _dry_run(self, **kwargs) -> bool:
        """Sends a dry run to the Flow to validate if the Flow is ready to receive requests

        :param kwargs: kwargs coming from the public interface. Includes arguments to be passed to the `WebsocketClientlet`
        :return: boolean indicating the readiness of the Flow
        """
        async with AsyncExitStack() as stack:
            try:
                proto = 'wss' if self.args.tls else 'ws'
                url = f'{proto}://{self.args.host}:{self.args.port}/dry_run'
                iolet = await stack.enter_async_context(
                    WebsocketClientlet(url=url, logger=self.logger, **kwargs)
                )

                async def _receive():
                    try:
                        async for response in iolet.recv_dry_run():
                            return response
                    except Exception as exc:
                        self.logger.error(
                            f'Error while fetching response from Websocket server {exc!r}'
                        )
                        raise

                async def _send():
                    return await iolet.send_dry_run()

                receive_task = asyncio.create_task(_receive())

                if receive_task.done():
                    raise RuntimeError(
                        'receive task not running, can not send messages'
                    )
                try:
                    send_task = asyncio.create_task(_send())
                    _, response_result = await asyncio.gather(send_task, receive_task)
                    if response_result.proto.code == jina_pb2.StatusProto.SUCCESS:
                        return True
                finally:
                    if iolet.close_code == status.WS_1011_INTERNAL_ERROR:
                        raise ConnectionError(iolet.close_message)
                    await receive_task

            except Exception as e:
                self.logger.error(
                    f'Error while getting response from websocket server {e!r}'
                )
            return False

    async def _get_results(
        self,
        inputs: 'InputType',
        on_done: 'CallbackFnType',
        on_error: Optional['CallbackFnType'] = None,
        on_always: Optional['CallbackFnType'] = None,
        **kwargs,
    ):
        """
        :param inputs: the callable
        :param on_done: the callback for on_done
        :param on_error: the callback for on_error
        :param on_always: the callback for on_always
        :param kwargs: kwargs coming from the public interface. Includes arguments to be passed to the `WebsocketClientlet`
        :yields: generator over results
        """
        with ImportExtensions(required=True):
            import aiohttp

        self.inputs = inputs
        request_iterator = self._get_requests(**kwargs)

        async with AsyncExitStack() as stack:
            cm1 = ProgressBar(
                total_length=self._inputs_length, disable=not (self.show_progress)
            )
            p_bar = stack.enter_context(cm1)

            proto = 'wss' if self.args.tls else 'ws'
            url = f'{proto}://{self.args.host}:{self.args.port}/'
            iolet = await stack.enter_async_context(
                WebsocketClientlet(url=url, logger=self.logger, **kwargs)
            )

            request_buffer: Dict[
                str, asyncio.Future
            ] = dict()  # maps request_ids to futures (tasks)

            def _result_handler(result):
                return result

            async def _receive():
                def _response_handler(response):
                    if response.header.request_id in request_buffer:
                        future = request_buffer.pop(response.header.request_id)
                        future.set_result(response)
                    else:
                        self.logger.warning(
                            f'discarding unexpected response with request id {response.header.request_id}'
                        )

                """Await messages from WebsocketGateway and process them in the request buffer"""
                try:
                    async for response in iolet.recv_message():
                        _response_handler(response)
                finally:
                    if request_buffer:
                        self.logger.warning(
                            f'{self.__class__.__name__} closed, cancelling all outstanding requests'
                        )
                        for future in request_buffer.values():
                            future.cancel()
                        request_buffer.clear()

            def _handle_end_of_iter():
                """Send End of iteration signal to the Gateway"""
                asyncio.create_task(iolet.send_eoi())

            def _request_handler(
                request: 'Request',
            ) -> 'Tuple[asyncio.Future, Optional[asyncio.Future]]':
                """
                For each request in the iterator, we send the `Message` using `iolet.send_message()`.
                For websocket requests from client, for each request in the iterator, we send the request in `bytes`
                using using `iolet.send_message()`.
                Then add {<request-id>: <an-empty-future>} to the request buffer.
                This empty future is used to track the `result` of this request during `receive`.
                :param request: current request in the iterator
                :return: asyncio Future for sending message
                """
                future = get_or_reuse_loop().create_future()
                request_buffer[request.header.request_id] = future
                asyncio.create_task(iolet.send_message(request))
                return future, None

            streamer = RequestStreamer(
                args=self.args,
                request_handler=_request_handler,
                result_handler=_result_handler,
                end_of_iter_handler=_handle_end_of_iter,
            )

            receive_task = asyncio.create_task(_receive())

            if receive_task.done():
                raise RuntimeError('receive task not running, can not send messages')
            try:
                async for response in streamer.stream(request_iterator):
                    callback_exec(
                        response=response,
                        on_error=on_error,
                        on_done=on_done,
                        on_always=on_always,
                        continue_on_error=self.continue_on_error,
                        logger=self.logger,
                    )
                    if self.show_progress:
                        p_bar.update()
                    yield response
            finally:
                if iolet.close_code == status.WS_1011_INTERNAL_ERROR:
                    raise ConnectionError(iolet.close_message)
                await receive_task

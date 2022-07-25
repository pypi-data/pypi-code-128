import click
import functools
import re
import sys
from asyncio import iscoroutinefunction
from click.types import convert_type
from contextlib import contextmanager
from neuro_cli.asyncio_utils import Runner
from neuro_sdk import ResourceNotFound
from typing import Any, Awaitable, Callable, Iterator, TypeVar

from neuro_flow.storage.base import Storage


@contextmanager
def _runner() -> Iterator[Runner]:
    # Suppress prints unhandled exceptions
    # on event loop closing to overcome aiohttp bug
    # Check https://github.com/aio-libs/aiohttp/issues/4324
    try:
        with Runner() as runner:
            yield runner
            sys.stderr = None  # type: ignore
    finally:
        sys.stderr = sys.__stderr__


_T = TypeVar("_T")


def wrap_async(
    pass_obj: bool = True, init_client: bool = True
) -> Callable[[Callable[..., Awaitable[_T]]], Callable[..., _T]]:
    def _decorator(callback: Callable[..., Awaitable[_T]]) -> Callable[..., _T]:
        assert iscoroutinefunction(callback)

        @functools.wraps(callback)
        def wrapper(*args: Any, **kwargs: Any) -> _T:
            with _runner() as runner:
                return runner.run(callback(*args, **kwargs))

        if pass_obj:
            wrapper = click.pass_obj(wrapper)

        return wrapper

    return _decorator


def option(*param_decls: Any, **attrs: Any) -> Callable[..., Any]:
    option_attrs = attrs.copy()
    typ = convert_type(attrs.get("type"), attrs.get("default"))
    autocompletion = getattr(typ, "complete", None)
    option_attrs.setdefault("shell_complete", autocompletion)
    return click.option(*param_decls, **option_attrs)


def argument(*param_decls: Any, **attrs: Any) -> Callable[..., Any]:
    arg_attrs = attrs.copy()
    typ = convert_type(attrs.get("type"), attrs.get("default"))
    autocompletion = getattr(typ, "complete", None)
    arg_attrs.setdefault("shell_complete", autocompletion)
    return click.argument(*param_decls, **arg_attrs)


BAKE_ID_PATTERN = r"bake-[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}"


async def resolve_bake(id_or_name: str, *, project: str, storage: Storage) -> str:
    if re.fullmatch(BAKE_ID_PATTERN, id_or_name):
        return id_or_name
    try:
        bake = await storage.project(yaml_id=project).bake(name=id_or_name).get()
        return bake.id
    except ResourceNotFound:
        return id_or_name

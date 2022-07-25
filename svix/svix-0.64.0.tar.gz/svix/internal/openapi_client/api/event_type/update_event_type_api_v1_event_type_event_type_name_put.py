import random
from time import sleep
from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...models.event_type_out import EventTypeOut
from ...models.event_type_update import EventTypeUpdate
from ...models.http_error import HttpError
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset


def _get_kwargs(
    event_type_name: str,
    *,
    client: AuthenticatedClient,
    json_body: EventTypeUpdate,
    idempotency_key: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/event-type/{event_type_name}/".format(client.base_url, event_type_name=event_type_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(idempotency_key, Unset) and idempotency_key is not None:
        headers["idempotency-key"] = idempotency_key

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> EventTypeOut:
    if response.status_code == 401:
        raise HttpError(response.json(), response.status_code)
    if response.status_code == 403:
        raise HttpError(response.json(), response.status_code)
    if response.status_code == 404:
        raise HttpError(response.json(), response.status_code)
    if response.status_code == 409:
        raise HttpError(response.json(), response.status_code)
    if response.status_code == 422:
        raise HTTPValidationError(response.json(), response.status_code)
    if response.status_code == 429:
        raise HttpError(response.json(), response.status_code)
    response_200 = EventTypeOut.from_dict(response.json())

    return response_200


sleep_time = 0.05
num_retries = 3


def sync_detailed(
    event_type_name: str,
    *,
    client: AuthenticatedClient,
    json_body: EventTypeUpdate,
    idempotency_key: Union[Unset, None, str] = UNSET,
) -> EventTypeOut:
    """Update Event Type

     Update an event type.

    Args:
        event_type_name (str):  Example: user.signup.
        idempotency_key (Union[Unset, None, str]): The request's idempotency key
        json_body (EventTypeUpdate):

    Returns:
        EventTypeOut
    """

    kwargs = _get_kwargs(
        event_type_name=event_type_name,
        client=client,
        json_body=json_body,
        idempotency_key=idempotency_key,
    )

    kwargs["headers"] = {"svix-req-id": f"{random.getrandbits(32)}", **kwargs["headers"]}

    retry_count = 0
    for retry in range(num_retries):
        response = httpx.request(
            verify=client.verify_ssl,
            **kwargs,
        )
        if response.status_code >= 500 and retry < num_retries:
            retry_count += 1
            kwargs["headers"]["svix-retry-count"] = str(retry_count)
            sleep(sleep_time)
            sleep_time * 2
        else:
            break

    return _parse_response(response=response)


def sync(
    event_type_name: str,
    *,
    client: AuthenticatedClient,
    json_body: EventTypeUpdate,
    idempotency_key: Union[Unset, None, str] = UNSET,
) -> EventTypeOut:
    """Update Event Type

     Update an event type.

    Args:
        event_type_name (str):  Example: user.signup.
        idempotency_key (Union[Unset, None, str]): The request's idempotency key
        json_body (EventTypeUpdate):

    Returns:
        EventTypeOut
    """

    return sync_detailed(
        event_type_name=event_type_name,
        client=client,
        json_body=json_body,
        idempotency_key=idempotency_key,
    )


async def asyncio_detailed(
    event_type_name: str,
    *,
    client: AuthenticatedClient,
    json_body: EventTypeUpdate,
    idempotency_key: Union[Unset, None, str] = UNSET,
) -> EventTypeOut:
    """Update Event Type

     Update an event type.

    Args:
        event_type_name (str):  Example: user.signup.
        idempotency_key (Union[Unset, None, str]): The request's idempotency key
        json_body (EventTypeUpdate):

    Returns:
        EventTypeOut
    """

    kwargs = _get_kwargs(
        event_type_name=event_type_name,
        client=client,
        json_body=json_body,
        idempotency_key=idempotency_key,
    )

    kwargs["headers"] = {"svix-req-id": f"{random.getrandbits(32)}", **kwargs["headers"]}

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        retry_count = 0
        for retry in range(num_retries):
            response = await _client.request(**kwargs)
            if response.status_code >= 500 and retry < num_retries:
                retry_count += 1
                kwargs["headers"]["svix-retry-count"] = str(retry_count)
                sleep(sleep_time)
                sleep_time * 2
            else:
                break

    return _parse_response(response=response)


async def asyncio(
    event_type_name: str,
    *,
    client: AuthenticatedClient,
    json_body: EventTypeUpdate,
    idempotency_key: Union[Unset, None, str] = UNSET,
) -> EventTypeOut:
    """Update Event Type

     Update an event type.

    Args:
        event_type_name (str):  Example: user.signup.
        idempotency_key (Union[Unset, None, str]): The request's idempotency key
        json_body (EventTypeUpdate):

    Returns:
        EventTypeOut
    """

    return await asyncio_detailed(
        event_type_name=event_type_name,
        client=client,
        json_body=json_body,
        idempotency_key=idempotency_key,
    )

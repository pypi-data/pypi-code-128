from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_script_by_hash_response_200 import GetScriptByHashResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    workspace: str,
    hash_: str,
) -> Dict[str, Any]:
    url = "{}/w/{workspace}/scripts/get/h/{hash}".format(client.base_url, workspace=workspace, hash=hash_)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetScriptByHashResponse200]:
    if response.status_code == 200:
        response_200 = GetScriptByHashResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetScriptByHashResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    workspace: str,
    hash_: str,
) -> Response[GetScriptByHashResponse200]:
    kwargs = _get_kwargs(
        client=client,
        workspace=workspace,
        hash_=hash_,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    workspace: str,
    hash_: str,
) -> Optional[GetScriptByHashResponse200]:
    """ """

    return sync_detailed(
        client=client,
        workspace=workspace,
        hash_=hash_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    workspace: str,
    hash_: str,
) -> Response[GetScriptByHashResponse200]:
    kwargs = _get_kwargs(
        client=client,
        workspace=workspace,
        hash_=hash_,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    workspace: str,
    hash_: str,
) -> Optional[GetScriptByHashResponse200]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            workspace=workspace,
            hash_=hash_,
        )
    ).parsed

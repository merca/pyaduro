"""Aduro session
"""
from __future__ import annotations

from typing import Any, Dict

import aiohttp  # pylint: disable=import-error #noqa F401

from aduro.const import API_VERSION, BASE_URL, CONTENT_TYPE_JSON
from aduro.exceptions import AduroResponseError
from aduro.model import SearchResponse


class AduroSession:  # pylint: disable=too-few-public-methods
    """
    Aduro session class
    """

    def __init__(
        self, session_id: str, session: aiohttp.ClientSession | None = None
    ) -> None:
        """Initialize Aduro session.

        :param session_id: session_id. Get this with AduroClient.login()
        :type session_id: str
        :param session: aiohttp client session, defaults to None and will be created
        :type session: aiohttp.ClientSession | None, optional
        """
        self._session = session or aiohttp.ClientSession()
        self._session_id = session_id

    def _get_headers(self) -> Dict[str, str]:
        """Get headers for request.

        :return: default headers
        """

        headers = {"Content-Type": CONTENT_TYPE_JSON, "X-Session": f"{self._session_id}"}
        return headers

    async def _get_url(self, path, params: dict | None = None) -> Dict[str, Any] | None:
        """Get data from url.

        :param path: Url path
        :type path: str
        :raises AduroResponseError:
        If response is not 200, raise exception with message from response
        :return: json response
        :rtype: dict[str, Any]
        """
        async with self._session.get(
            f"{BASE_URL}/{API_VERSION}/{path}", params=params, headers=self._get_headers()
        ) as resp:
            data = await resp.json()
            if resp.status != 200:
                raise AduroResponseError(
                    f"Error getting stove ID: {data['message']}")
            return data

    async def _post_url(self, path, data) -> Dict[str, Any] | None:
        """Post data to url.

        :param path: Url path
        :type path: str
        :param data: Data to post
        :type data: dict[str, Any]
        :raises AduroResponseError:
        If response is not 200, raise exception with message from response
        :return: json response
        :rtype: dict[str, Any]
        """
        async with self._session.post(
            f"{BASE_URL}/{API_VERSION}/{path}", headers=self._get_headers(), json=data
        ) as resp:
            data = await resp.json()
            if resp.status != 200:
                raise AduroResponseError(
                    f"Error getting stove ID: {data['message']}")
            return data

    async def async_get_stove_ids(self, stove_name="Stove") -> list[str] | None:
        """Get stove ids. Should absolutely return only one.

        :param stove_name: The device name in Wappsto, defaults to "Stove"
        :type stove_name: str, optional
        :raises AduroResponseError: If api response is not 200
        :return: list of stove ids
        :rtype: List[str] | None
        """
        raw = await self._get_url(
            path="device",
            params={"this_manufacturer": "Aduro",
                    "this_name": f"{stove_name}"},
        )
        data = SearchResponse(**raw) if raw else None
        return data.id if data else None

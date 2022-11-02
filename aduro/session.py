"""Aduro session"""
from __future__ import annotations

import json
from typing import Any, Dict

import aiohttp  # pylint: disable=import-error #noqa F401

from aduro.const import API_VERSION, BASE_URL, CONTENT_TYPE_JSON
from aduro.datetime_encoder import DateTimeEncoder
from aduro.exceptions import AduroResponseError
from aduro.model import Device, Entity, SearchResponse, State, StateType


class AduroSession:  # pylint: disable=too-few-public-methods
    """Aduro session class"""

    def __init__(
        self,
        session_id: str,
    ) -> None:
        """Initialize Aduro session.

        :param session_id: session_id. Get this with AduroClient.login()
        :type session_id: str
        :param session: aiohttp client session, defaults to None and will be created
        :type session: aiohttp.ClientSession | None, optional
        """

        self._session = aiohttp.ClientSession(
            json_serialize=lambda object: json.dumps(
                object,
                cls=DateTimeEncoder,
            ),
        )
        self._session_id = session_id

    def _get_headers(self) -> Dict[str, str]:
        """Get headers for request.

        :return: default headers
        """

        headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "X-Session": f"{self._session_id}",
        }
        return headers

    async def _get_url(
        self,
        path: str,
        params: dict | None = None,
    ) -> Dict[str, Any] | None:
        """Get data from url.

        :param path: Url path
        :type path: str
        :raises AduroResponseError:
        If response is not 200, raise exception with message from response
        :return: json response
        :rtype: dict[str, Any]
        """
        async with self._session.get(
            f"{BASE_URL}/{API_VERSION}/{path}",
            params=params,
            headers=self._get_headers(),
        ) as resp:
            data = await resp.json()
            if resp.status != 200:
                raise AduroResponseError(
                    f"Error getting stove ID: {data['message']}",
                )
            return data

    async def _patch_url(
        self,
        path: str,
        data: Dict[str, Any],
    ) -> Dict[str, Any] | None:
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
        async with self._session.patch(
            f"{BASE_URL}/{API_VERSION}/{path}",
            headers=self._get_headers(),
            json=data,
        ) as resp:
            response = await resp.json()
            if resp.status != 200:
                raise AduroResponseError(
                    f"Error patching object: {response['message']}",
                )
            return response

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
            params={
                "this_manufacturer": "Aduro",
                "this_name": f"{stove_name}",
            },
        )
        data = SearchResponse(**raw) if raw else None
        return data.id if data else None

    async def aync_get_device_info(self, device_id: str) -> Device | None:
        """Get devices.

        :return: Device
        :rtype: Device
        """
        data = await self._get_url(f"device/{device_id}")
        return Device(**data) if data else None

    async def async_get_device_entities(
        self,
        ids: list[str],
    ) -> list[Entity] | list[Any]:
        """Get device entities (called values in Wappsto)

        :param device_id: device id
        :type device_id: str
        :return: list of entities
        :rtype: list[Entity] | None
        """
        entities = []
        for entity_id in ids:
            data = await self._get_url(f"value/{entity_id}")
            entity = Entity(**data) if data else None
            entities.append(entity)
        return entities

    async def async_get_state_value(self, state_id: str) -> State | None:
        """Get entity state

        :param state_id: state id
        :type state_id: str
        :return: Entity state
        :rtype: State
        """
        data = await self._get_url(f"state/{state_id}")
        return State(**data) if data else None

    async def async_patch_state_value(
        self,
        state_id: str,
        value: Any,
        state_type: StateType,
    ) -> bool:
        """Pathes the state value

        :param state_id: The id for the state
        :type state_id: str
        :param value: The desired value
        :type value: Any
        :param state_type: The type of the state
        :type state_type: StateType
        :raises AduroResponseError: If stete type is not supported
        :return: true if success
        :rtype: bool
        """
        if state_type != StateType.CONTROL:
            raise AduroResponseError("Can only update control state")
        payload = {
            "data": value,
            "type": state_type.value,
        }
        await self._patch_url(f"state/{state_id}", payload)
        return True

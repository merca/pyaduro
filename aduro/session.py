"""Aduro session for request handling"""
from __future__ import annotations
from typing import Dict, List

from aduro.exceptions import AduroResponseError

from .const import API_VERSION, BASE_URL, CONTENT_TYPE_JSON
from .version import __version__


class AduroSession:
    """
        Aduro session class
    """

    def __init__(self, session, session_id):
        """Initialize AduroSession class."""
        self._session = session
        self._session_id = session_id

    def __repr__(self) -> str:
        """Representation of AduroSession class."""
        return f"AduroSession version {__version__}"

    def _get_headers(self) -> Dict[str, str]:
        """Return headers."""
        headers = {"Content-Type": CONTENT_TYPE_JSON}
        if self._session_id:
            headers["X-Session"] = f"{self._session_id}"
        return headers

    async def async_get_stove_ids(self, stove_name="Stove") -> List[str] | None:
        """
        Async method to get stove IDs. It uses `Aduro` as manufacturer and `Stove` as name.
        This should return only one instance, but in case there are more,
        it will return all of them and you have to find the correct one.

        Returns:
            List[str] | None: Stove ID or None if not found.

        Raises:
            AduroResponseError: if response is not 200.

        """
        async with self._session.get(
            f"{BASE_URL}/{API_VERSION}/device",
            params={"this_manufacturer": "Aduro",
                    "this_name": f"{stove_name}"},
            headers=self._get_headers(),
        ) as resp:
            data = await resp.json()
            if resp.status != 200:
                raise AduroResponseError(
                    f"Error getting stove ID: {data['message']}")
            count = len(list(data["id"]))
            if count == 1:
                return data["id"]
            if count == 0:
                return None

"""Unit tests for the Session class."""

from unittest.mock import patch

import aiohttp  # pylint: disable=import-error # noqa: F401
import pytest  # pylint: disable=import-error # noqa: F401

from aduro.exceptions import AduroResponseError
from aduro.session import AduroSession


class MockResponse:
    """Mock response class."""

    def __init__(self, response_json, status):
        """Initialize MockResponse class."""
        self._json = response_json
        self.status = status

    async def json(self):
        """Return json object."""
        return self._json

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
    ):  # pylint: disable=unused-argument, invalid-name # noqa: E501, E261
        pass

    async def __aenter__(self):
        return self


class TestSession:
    """Test the Session class."""

    @staticmethod
    def successful_response():
        """Return a successful response."""
        return MockResponse({"success": True}, 200)

    @staticmethod
    def unsuccessful_response():
        """Return an unsuccessful response."""
        return MockResponse({"message": "request failed"}, 400)

    @pytest.mark.asyncio
    async def test_successful_get(self):
        """Test get with resonse code 200."""
        data = {"success": True}
        aduro_session = AduroSession("session_id")
        with patch.object(
            aiohttp.ClientSession,
            "get",
            return_value=self.successful_response(),
        ):
            result = await aduro_session._get_url(  # pylint: disable=protected-access
                "test_url",
            )
        assert result == data

    @pytest.mark.asyncio
    async def test_unsuccessful_get(self):
        """Test get with response code 400."""
        aduro_session = AduroSession("session_id")
        with patch.object(
            aiohttp.ClientSession,
            "get",
            return_value=self.unsuccessful_response(),
        ), pytest.raises(AduroResponseError):
            await aduro_session._get_url("test_url")  # pylint: disable=protected-access

    @pytest.mark.asyncio
    async def test_successful_patch(self):
        """Test put with response code 200."""
        data = {"success": True}
        aduro_session = AduroSession("session_id")
        with patch.object(
            aiohttp.ClientSession,
            "patch",
            return_value=self.successful_response(),
        ):
            result = await aduro_session._patch_url(  # pylint: disable=protected-access
                "test_url",
                data,
            )
            assert result == data

    @pytest.mark.asyncio
    async def test_unsuccessful_patch(self):
        """Test post with response code 400."""
        aduro_session = AduroSession("session_id")
        data = {"test": "test"}
        with patch.object(
            aiohttp.ClientSession,
            "patch",
            return_value=self.unsuccessful_response(),
        ), pytest.raises(AduroResponseError):
            await aduro_session._patch_url(  # pylint: disable=protected-access
                "test_url",
                data=data,
            )

"""Unit tests for the Session class."""

from unittest.mock import patch

import aiohttp
import pytest

from aduro.exceptions import AduroResponseError
from aduro.session import AduroSession


class MockResponse:
    """Mock response class."""

    def __init__(self, response_json, status):
        self._json = response_json
        self.status = status

    async def json(self):
        """Return json object."""
        return self._json

    async def __aexit__(
        self, exc_type, exc, tb
    ):  # pylint: disable=unused-argument, invalid-name # noqa: E501, E261
        pass

    async def __aenter__(self):
        return self


class TestSession:
    """Test the Session class."""

    def successfull_response(self):
        """Return a successfull response."""
        return MockResponse({"success": True}, 200)

    def unsuccessfull_response(self):
        """Return an unsuccessfull response."""
        return MockResponse({"message": "request failed"}, 400)

    @pytest.mark.asyncio
    async def test_succesfull_get(self):
        """Test get."""
        data = {"success": True}
        aduro_session = AduroSession("session_id", aiohttp.ClientSession())
        with patch.object(
            aiohttp.ClientSession, "get", return_value=self.successfull_response()
        ):
            result = await aduro_session._get_url(  # pylint: disable=protected-access
                "test_url"
            )
        assert result == data

    @pytest.mark.asyncio
    async def test_unsuccesfull_get(self):
        """Test get."""
        aduro_session = AduroSession("session_id", aiohttp.ClientSession())
        with patch.object(
            aiohttp.ClientSession, "get", return_value=self.unsuccessfull_response()
        ):
            with pytest.raises(AduroResponseError):
                await aduro_session._get_url(  # pylint: disable=protected-access
                    "test_url"
                )

    @pytest.mark.asyncio
    async def test_succesfull_post(self):
        """Test post."""
        data = {"success": True}
        aduro_session = AduroSession("session_id", aiohttp.ClientSession())
        with patch.object(
            aiohttp.ClientSession, "post", return_value=self.successfull_response()
        ):
            result = await aduro_session._post_url(  # pylint: disable=protected-access
                "test_url", data
            )
            assert result == data

    @pytest.mark.asyncio
    async def test_unsuccesfull_post(self):
        """Test post."""
        aduro_session = AduroSession("session_id", aiohttp.ClientSession())
        with patch.object(
            aiohttp.ClientSession, "post", return_value=self.unsuccessfull_response()
        ):
            with pytest.raises(AduroResponseError):
                await aduro_session._post_url(  # pylint: disable=protected-access
                    "test_url", {}
                )

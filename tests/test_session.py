"""Unit tests for the Session class."""

import aiohttp
import pytest

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


@pytest.fixture(name="aduro_session")
async def session_fixture():
    """Session fixture."""
    async with aiohttp.ClientSession() as session:
        yield AduroSession("session_id", session)


@pytest.mark.asyncio
async def test_succesfull_get(mocker):
    """Test get."""
    data = {"test": "test"}
    response = MockResponse(data, 200)
    aduro_session = AduroSession("session_id", aiohttp.ClientSession())
    with mocker.patch("aiohttp.ClientSession.get", return_value=response):
        result = await aduro_session._get_url(
            "test"
        )  # pylint: disable=protected-access # noqa: E501, E261
        assert result == data


@pytest.mark.asyncio
async def test_unsuccesfull_get(mocker):
    """Test get."""
    data = {"message": "test"}
    response = MockResponse(data, 400)
    aduro_session = AduroSession("session_id", aiohttp.ClientSession())
    with mocker.patch("aiohttp.ClientSession.get", return_value=response):
        with pytest.raises(Exception):
            await aduro_session._get_url(
                "test"
            )  # pylint: disable=protected-access # noqa: E501, E261


@pytest.mark.asyncio
async def test_succesfull_post(mocker):
    """Test get."""
    data = {"test": "test"}
    response = MockResponse(data, 200)
    aduro_session = AduroSession("session_id", aiohttp.ClientSession())
    with mocker.patch("aiohttp.ClientSession.post", return_value=response):
        result = await aduro_session._post_url(
            "test", data
        )  # pylint: disable=protected-access # noqa: E501, E261
        assert result == data


@pytest.mark.asyncio
async def test_unsuccesfull_post(mocker):
    """Test get."""
    data = {"message": "test"}
    response = MockResponse(data, 400)
    aduro_session = AduroSession("session_id", aiohttp.ClientSession())
    with mocker.patch("aiohttp.ClientSession.post", return_value=response):
        with pytest.raises(Exception):
            await aduro_session._post_url(
                "test", data
            )  # pylint: disable=protected-access # noqa: E501, E261

"""
    Test the AduroSession class.
"""
import aiohttp  # noqa E402 # pylint: disable=import-error
import pytest
from aduro.exceptions import AduroResponseError  # noqa E402 # pylint: disable=import-error

from aduro.session import AduroSession


@pytest.fixture(name="session_id")
def get_session_id():
    """Return a session ID."""
    return "61b2f7c8-d9be-42e6-8c50-fe93482a8409"


@pytest.mark.asyncio
async def test_get_session_header_has_session_id(session_id):
    """Test the get session header method."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, session_id)
        headers = aduro_session._get_headers()  # pylint: disable=protected-access
        assert headers["X-Session"] == session_id


@pytest.mark.asyncio
async def test_get_session_header_has_no_session_id():
    """Test the get session header method."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, None)
        headers = aduro_session._get_headers()  # pylint: disable=protected-access
        assert "X-Session" not in headers


@pytest.mark.asyncio
async def test_module_version():
    """Test the module version."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, None)
        assert repr(
            aduro_session) == "AduroSession version 0.1.0-beta-1"


@pytest.mark.asyncio
async def test_get_stove_id_with_unknown_session_id_raises_aduro_response_error():
    """Test getting the stove ID."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, "session_id")
        with pytest.raises(AduroResponseError):
            await aduro_session.async_get_stove_ids()


@pytest.mark.asyncio
async def test_get_stove_id_no_stove(session_id):
    """Test getting the stove ID."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, session_id)
        assert await aduro_session.async_get_stove_ids("bongo") is None

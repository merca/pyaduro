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
    return "28971e75-86d4-4d6c-ae17-7b23944ecdd6"


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
async def test_get_stove_id_raises_aduro_response_error():
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


@pytest.mark.asyncio
async def test_get_stove_details(session_id):
    """Test getting the stove details."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, session_id)
        stove = await aduro_session.get_stove_details("797f71cb-504b-4197-ac60-4643358046da")
        assert stove is not None
        assert stove.meta.id == "797f71cb-504b-4197-ac60-4643358046da"
        assert stove.name == "Stove"
        assert stove.manufacturer == "Aduro"
        assert stove.product == "P1 [4DFA]"
        assert isinstance(stove.value, list)
        assert "f7143fd8-b809-48d7-96a9-39ffc6f525ad" in stove.value


@pytest.mark.asyncio
async def test_get_stove_details_raises_aduro_response_error():
    """Test getting the stove details."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, "session_id")
        with pytest.raises(AduroResponseError):
            await aduro_session.get_stove_details("797f71cb-504b-4197-ac60-4643358046da")

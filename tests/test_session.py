"""
    Test the AduroSession class.
"""
import aiohttp  # noqa E402 # pylint: disable=import-error
import pytest  # noqa E402 # pylint: disable=import-error

from aduro.session import AduroSession


@pytest.fixture(name="session_id")
def get_session_id():
    """Return a session ID."""
    return "61b2f7c8-d9be-42e6-8c50-fe93482a8409"


@pytest.mark.asyncio
async def test_get_session_header(session_id):
    """Test the get session header method."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, session_id)
        headers = aduro_session._get_headers()  # pylint: disable=protected-access
        assert headers["X-Session"] == session_id


@pytest.mark.asyncio
async def test_get_stove_id(session_id):
    """Test getting the stove ID."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, session_id)
        assert await aduro_session.async_get_stove_ids() == ["797f71cb-504b-4197-ac60-4643358046da"]

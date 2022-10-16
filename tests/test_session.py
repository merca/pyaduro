"""
    Test the AduroSession class.
"""
import aiohttp
import pytest

from aduro.session import AduroSession


@pytest.fixture(name="session_id")
def get_session_id():
    """Return a session ID."""
    return "61b2f7c8-d9be-42e6-8c50-fe93482a8409"


@pytest.mark.asyncio
async def test_get_stove_id(session_id):
    """Test getting the stove ID."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session, session_id)
        assert await aduro_session.async_get_stove_ids() == ["797f71cb-504b-4197-ac60-4643358046da"]

"""Integration testing for Aduro API."""

import aiohttp  # pylint: disable=import-error
import pytest  # pylint: disable=import-error

from aduro.session import AduroSession
from aduro.exceptions import AduroResponseError


@pytest.fixture(name="session_id")
def get_session_id():
    """Return a session ID."""
    return "98c9b32d-b17e-4176-9e47-623fd7579c81"


@pytest.mark.asyncio
async def test_get_successful_stove_id(session_id):
    """Test getting the stove ID."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session_id, session)
        stove_ids = await aduro_session.async_get_stove_ids()
        assert (
            "797f71cb-504b-4197-ac60-4643358046da" in stove_ids if stove_ids else False
        )


@pytest.mark.asyncio
async def test_get_stove_id_no_stove(session_id):
    """Test getting the stove ID."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session_id, session)
        assert await aduro_session.async_get_stove_ids("bongo") == []


@pytest.mark.asyncio
async def test_get_stove_id_with_unknown_session_id_raises_aduro_response_error():
    """Test getting the stove ID."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession("session_id", session)
        with pytest.raises(AduroResponseError):
            await aduro_session.async_get_stove_ids()

@pytest.mark.asyncio

async def test_successful_get_device_info(session_id):
    """Test getting the device info."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session_id, session)
        device_info = await aduro_session.aync_get_device_info(
            "797f71cb-504b-4197-ac60-4643358046da"
        )
        assert device_info is not None


@pytest.mark.asyncio
async def test_get_device_info_with_unknown_session_id_raises_aduro_response_error():
    """Test getting the device info."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession("session_id", session)
        with pytest.raises(AduroResponseError):
            await aduro_session.aync_get_device_info("797f71cb-504b-4197-ac60-4643358046da")


@pytest.mark.asyncio
async def test_get_device_info_with_unknown_stove_id_raises_aduro_response_error(session_id):
    """Test getting the device info."""
    async with aiohttp.ClientSession() as session:
        aduro_session = AduroSession(session_id, session)
            await aduro_session.aync_get_device_info("bongo")
        with pytest.raises(AduroResponseError):
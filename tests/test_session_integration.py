"""Integration testing for Aduro API."""
import os
from datetime import datetime

import pytest  # pylint: disable=import-error
from dotenv import load_dotenv  # pylint: disable=import-error

from aduro.exceptions import AduroResponseError
from aduro.model import StateType
from aduro.session import AduroSession


@pytest.fixture(name="session_id")
def get_session_id():
    """Return a session ID."""
    load_dotenv()
    return os.getenv("SESSION_ID")


@pytest.mark.asyncio
async def test_get_successful_stove_id(session_id):
    """Test getting the stove ID."""
    aduro_session = AduroSession(session_id)
    stove_ids = await aduro_session.async_get_stove_ids()
    assert "373371fe-9735-4069-25d6-44a93531a982" in stove_ids if stove_ids else False


@pytest.mark.asyncio
async def test_get_stove_id_no_stove(session_id):
    """Test getting the stove ID."""
    aduro_session = AduroSession(session_id)
    assert await aduro_session.async_get_stove_ids("bongo") == []


@pytest.mark.asyncio
async def test_get_stove_id_with_unknown_session_id_raises_aduro_response_error():
    """Test getting the stove ID."""
    aduro_session = AduroSession("session_id")
    with pytest.raises(AduroResponseError):
        await aduro_session.async_get_stove_ids()


@pytest.mark.asyncio
async def test_successful_get_device_info(session_id):
    """Test getting the device info."""
    aduro_session = AduroSession(session_id)
    device_info = await aduro_session.aync_get_device_info(
        "373371fe-9735-4069-25d6-44a93531a982",
    )
    assert device_info is not None


@pytest.mark.asyncio
async def test_get_device_info_with_unknown_session_id_raises_aduro_response_error():
    """Test getting the device info."""
    aduro_session = AduroSession("session_id")
    with pytest.raises(AduroResponseError):
        await aduro_session.aync_get_device_info(
            "373371fe-9735-4069-25d6-44a93531a982",
        )


@pytest.mark.asyncio
async def test_get_device_info_with_unknown_stove_id_raises_aduro_response_error(
    session_id,
):
    """Test getting the device info."""
    aduro_session = AduroSession(session_id)
    with pytest.raises(AduroResponseError):
        await aduro_session.aync_get_device_info("bongo")


@pytest.mark.asyncio
async def test_get_device_entities(session_id):
    """Test getting device entities"""
    aduro_session = AduroSession(session_id)
    device = await aduro_session.aync_get_device_info(
        "373371fe-9735-4069-25d6-44a93531a982",
    )
    entities = await aduro_session.async_get_device_entities(device.value)
    assert len(entities) == 40
    assert entities[0].name == "On/Off"
    assert entities[0].number is not None
    assert entities[0].number.unit == ""


@pytest.mark.asyncio
async def test_entity_state(session_id):
    """Test entity status"""
    aduro_session = AduroSession(session_id)
    device = await aduro_session.aync_get_device_info(
        "373371fe-9735-4069-25d6-44a93531a982",
    )
    entities = await aduro_session.async_get_device_entities(device.value)
    on_off_state = await aduro_session.async_get_state_value(entities[0].state[0])
    assert on_off_state.type == StateType.CONTROL


@pytest.mark.asyncio
async def test_update_state_value(session_id):
    """Test put by updating time on the stove"""
    state = None
    aduro_session = AduroSession(session_id)
    state = await aduro_session.async_get_state_value(
        "ed006fd8-3a86-4e60-1c37-bb688a079638",
    )
    assert state.type == StateType.CONTROL
    now = datetime.utcnow()
    result = await aduro_session.async_put_state_value(
        state.meta.id,
        now,
        state_type=state.type,
    )
    assert result is True


@pytest.mark.asyncio
async def test_update_state_value_with_unknown_state_id_raises_aduro_response_error(
    session_id,
):
    """Test put by updating time on the stove"""
    aduro_session = AduroSession(session_id)
    with pytest.raises(AduroResponseError):
        await aduro_session.async_put_state_value(
            "bongo",
            1,
            state_type=StateType.CONTROL,
        )


@pytest.mark.asyncio
async def test_update_state_value_with_report_state_type_raises_aduro_response_error(
    session_id,
):
    """Test put by updating time on the stove"""
    aduro_session = AduroSession(session_id)
    with pytest.raises(AduroResponseError):
        await aduro_session.async_put_state_value(
            "ed006fd8-3a86-4e60-1c37-bb688a079638",
            1,
            state_type=StateType.REPORT,
        )

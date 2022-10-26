"""Test Aduro api response models"""

from datetime import datetime, timezone

from aduro.model import Connection, Device, Entity, Meta, Number, SearchResponse, State

# pylint: disable=unused-import
from .model_fixtures import (
    get_connection_obj,
    get_device_obj,
    get_entity_number_obj,
    get_entity_string_obj,
    get_meta_obj,
    get_number_obj,
    get_search_response_obj,
    get_state_number_obj,
    get_state_string_obj,
)

# pylint: enable=unused-import

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


def test_connection_from_dict(connection_obj):
    """Test connection from dict"""
    connection = Connection(**connection_obj)
    assert connection.timestamp == datetime(
        2022, 10, 14, 16, 6, 22, 21852, tzinfo=timezone.utc
    )
    assert connection.online is False


def test_meta_from_dict(meta_obj):
    """Test meta from dict"""
    meta = Meta(**meta_obj)
    assert meta.id == "373371fe-9735-4069-25d6-44a93531a982"
    assert meta.type == "device"
    assert meta.version == "2.1"
    assert meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"
    assert meta.manufacturer == "d510770c-e8cc-4b9f-8863-6044b96bb799"
    assert meta.created == datetime(
        2022, 9, 14, 18, 39, 45, 340401, tzinfo=timezone.utc
    )
    assert meta.updated == datetime(
        2022, 10, 14, 9, 47, 25, 969650, tzinfo=timezone.utc
    )
    assert not meta.tag
    assert not meta.tag_by_user
    assert meta.name_by_user == "Stove"
    assert meta.iot is True
    assert meta.connection.timestamp == datetime(
        2022, 10, 14, 16, 6, 22, 21852, tzinfo=timezone.utc
    )
    assert meta.connection.online is False
    assert meta.stable_connection.timestamp == datetime(
        2022, 10, 14, 16, 6, 22, 21852, tzinfo=timezone.utc
    )
    assert meta.stable_connection.online is False


def test_device_from_dict(device_obj):
    """Test device from dict"""
    device = Device(**device_obj)
    assert not device.status
    assert device.value == [
        "309c0f56-280f-4e8d-8fe9-4dc8af8cbdbb",
        "a4e7a139-eb90-4c09-a8d0-760181f504dd",
    ]
    assert device.name == "Stove"
    assert device.manufacturer == "Aduro"
    assert device.product == "P1 [4EFA]"
    assert device.version == "1.2.9"
    assert device.serial == "1879"
    assert device.description == "Aduro Stove on Seluxit Echidna"
    assert device.protocol == "JSONRPC over SSL"
    assert device.communication == "WIFI"
    assert device.meta.id == "373371fe-9735-4069-25d6-44a93531a982"
    assert device.meta.type == "device"
    assert device.meta.version == "2.1"
    assert device.meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"


def test_number_from_dict(number_obj):
    """Test number from dict"""
    number = Number(**number_obj)
    assert number.min == 0.0
    assert number.max == 1.0
    assert number.step == 1.0
    assert number.unit == ""


def test_entity_number_obj(entity_number_obj):
    """Test entity number from dict"""
    entity_number = Entity(**entity_number_obj)
    assert entity_number.state == ["69d1f4fa-b664-46f2-321e-db6a7dc12776"]
    assert not entity_number.eventlog
    assert entity_number.name == "On/Off"
    assert entity_number.type == "boolean"
    assert entity_number.period == "0"
    assert entity_number.delta == "0.000000"
    assert entity_number.permission == "w"
    assert entity_number.number.min == 0.0
    assert entity_number.number.max == 1.0
    assert entity_number.number.step == 1.0
    assert entity_number.number.unit == ""
    assert entity_number.meta.id == "309c0f56-280f-4e8d-8fe9-4dc8af8cbdbb"
    assert entity_number.meta.type == "value"
    assert entity_number.meta.version == "2.1"
    assert entity_number.meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"
    assert entity_number.meta.manufacturer == "d510770c-e8cc-4b9f-8863-6044b96bb799"
    assert entity_number.meta.created == datetime(
        2022, 9, 14, 18, 39, 45, 340401, tzinfo=timezone.utc
    )
    assert entity_number.meta.updated == datetime(
        2022, 10, 5, 16, 51, 42, 810914, tzinfo=timezone.utc
    )
    assert not entity_number.meta.tag
    assert not entity_number.meta.tag_by_user
    assert entity_number.meta.name_by_user == "On/Off"


def test_entity_string_obj(entity_string_obj):
    """Test entity string from dict"""
    entity_string = Entity(**entity_string_obj)
    assert entity_string.state == ["a517d519-e326-4690-076e-115f6c632da6"]
    assert not entity_string.eventlog
    assert entity_string.name == "Status"
    assert entity_string.type == "aduro_state"
    assert entity_string.period == "0"
    assert entity_string.delta == "0.000000"
    assert entity_string.permission == "r"
    assert entity_string.string.encoding == ""
    assert entity_string.string.max == 10
    assert entity_string.meta.id == "a4e7a139-eb90-4c09-a8d0-760181f504dd"
    assert entity_string.meta.type == "value"
    assert entity_string.meta.version == "2.1"
    assert entity_string.meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"
    assert entity_string.meta.manufacturer == "d510770c-e8cc-4b9f-8863-6044b96bb799"
    assert entity_string.meta.created == datetime(
        2022, 9, 14, 18, 39, 45, 340401, tzinfo=timezone.utc
    )
    assert entity_string.meta.updated == datetime(
        2022, 10, 5, 16, 51, 42, 810914, tzinfo=timezone.utc
    )
    assert not entity_string.meta.tag
    assert not entity_string.meta.tag_by_user
    assert entity_string.meta.name_by_user == "Status"


def test_state_string_obj(state_string_obj):
    """Test state string from dict"""
    state_string = State(**state_string_obj)
    assert state_string.timestamp == datetime(
        2022, 10, 15, 16, 29, 17, 23096, tzinfo=timezone.utc
    )
    assert state_string.data == "WORK PHASE"
    assert state_string.status_payment == "owned"
    assert state_string.type == "Report"
    assert state_string.meta.id == "a517d519-e326-4690-076e-115f6c632da6"
    assert state_string.meta.type == "state"
    assert state_string.meta.version == "2.1"
    assert state_string.meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"
    assert state_string.meta.manufacturer == "d510770c-e8cc-4b9f-8863-6044b96bb799"
    assert state_string.meta.created == datetime(
        2022, 9, 14, 18, 39, 45, 340401, tzinfo=timezone.utc
    )
    assert state_string.meta.updated == datetime(
        2022, 10, 15, 16, 29, 17, 112739, tzinfo=timezone.utc
    )
    assert not state_string.meta.tag
    assert not state_string.meta.tag_by_user
    assert state_string.meta.name_by_user == "Report"
    assert state_string.meta.iot is True


def test_state_number_obj(state_number_obj):
    """Test state number from dict"""
    state_number = State(**state_number_obj)
    assert state_number.timestamp == datetime(
        2022, 10, 15, 16, 29, 15, 764136, tzinfo=timezone.utc
    )
    assert int(state_number.data) == 0
    assert state_number.status_payment == "owned"
    assert state_number.type == "Control"
    assert state_number.meta.id == "69d1f4fa-b664-46f2-321e-db6a7dc12776"
    assert state_number.meta.type == "state"
    assert state_number.meta.version == "2.1"
    assert state_number.meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"
    assert state_number.meta.manufacturer == "d510770c-e8cc-4b9f-8863-6044b96bb799"
    assert state_number.meta.created == datetime(
        2022, 9, 14, 18, 39, 45, 340401, tzinfo=timezone.utc
    )
    assert state_number.meta.updated == datetime(
        2022, 10, 15, 16, 29, 15, 987863, tzinfo=timezone.utc
    )
    assert not state_number.meta.tag
    assert not state_number.meta.tag_by_user
    assert state_number.meta.name_by_user == "Control"
    assert state_number.meta.iot is True


def test_search_response_obj(search_response_obj):
    """Test search response from dict"""
    search_response = SearchResponse(**search_response_obj)
    assert search_response.count == 1
    assert search_response.limit == 1000
    assert search_response.meta["type"] == "idlist"
    assert search_response.child[0]["type"] == "device"
    assert search_response.id == ["797f71cb-504b-4197-ac60-4643358046da"]

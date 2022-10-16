"""
Test Aduro api response models
"""

from datetime import datetime

from aduro.model import Connection, Device, Entity, Meta, Number, State

# pylint: disable=unused-import
from .fixtures import (get_connection_obj, get_device_obj,
                       get_entity_number_obj, get_entity_string_obj,
                       get_meta_obj, get_number_obj, get_state_number_obj,
                       get_state_string_obj)

# pylint: enable=unused-import

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


def test_connection_from_dict(connection_obj):
    """Test connection from dict"""
    connection = Connection.from_dict(connection_obj)
    assert connection.timestamp == datetime.strptime(
        "2022-10-14T16:06:22.021852Z", TIMESTAMP_FORMAT
    )
    assert connection.online is False


def test_meta_from_dict(meta_obj):
    """Test meta from dict"""
    meta = Meta.from_dict(meta_obj)
    assert meta.id == "373371fe-9735-4069-25d6-44a93531a982"
    assert meta.type == "device"
    assert meta.version == "2.1"
    assert meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"
    assert meta.manufacturer == "d510770c-e8cc-4b9f-8863-6044b96bb799"
    assert meta.created == datetime.strptime(
        "2022-09-14T18:39:45.340401Z", TIMESTAMP_FORMAT
    )
    assert meta.updated == datetime.strptime(
        "2022-10-14T09:47:25.969650Z", TIMESTAMP_FORMAT
    )
    assert not meta.tag
    assert not meta.tag_by_user
    assert meta.name_by_user == "Stove"
    assert meta.iot is True
    assert meta.connection.timestamp == datetime.strptime(
        "2022-10-14T16:06:22.021852Z", TIMESTAMP_FORMAT
    )
    assert meta.connection.online is False
    assert meta.stable_connection.timestamp == datetime.strptime(
        "2022-10-14T16:06:22.021852Z", TIMESTAMP_FORMAT
    )
    assert meta.stable_connection.online is False


def test_device_from_dict(device_obj):
    """Test device from dict"""
    device = Device.from_dict(device_obj)
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
    number = Number.from_dict(number_obj)
    assert number.min == 0.0
    assert number.max == 1.0
    assert number.step == 1.0
    assert number.unit == ""


def test_entity_number_obj(entity_number_obj):
    """Test entity number from dict"""
    entity_number = Entity.from_dict(entity_number_obj)
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
    assert entity_number.meta.created == datetime.strptime(
        "2022-09-14T18:39:45.340401Z", TIMESTAMP_FORMAT
    )
    assert entity_number.meta.updated == datetime.strptime(
        "2022-10-05T16:51:42.810914Z", TIMESTAMP_FORMAT
    )
    assert not entity_number.meta.tag
    assert not entity_number.meta.tag_by_user
    assert entity_number.meta.name_by_user == "On/Off"


def test_entity_string_obj(entity_string_obj):
    """Test entity string from dict"""
    entity_string = Entity.from_dict(entity_string_obj)
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
    assert entity_string.meta.created == datetime.strptime(
        "2022-09-14T18:39:45.340401Z", TIMESTAMP_FORMAT
    )
    assert entity_string.meta.updated == datetime.strptime(
        "2022-10-05T16:51:42.810914Z", TIMESTAMP_FORMAT
    )
    assert not entity_string.meta.tag
    assert not entity_string.meta.tag_by_user
    assert entity_string.meta.name_by_user == "Status"


def test_state_string_obj(state_string_obj):
    """Test state string from dict"""
    state_string = State.from_dict(state_string_obj)
    assert state_string.timestamp == datetime.strptime(
        "2022-10-15T16:29:17.023096Z", TIMESTAMP_FORMAT
    )
    assert state_string.data == "WORK PHASE"
    assert state_string.status_payment == "owned"
    assert state_string.type == "Report"
    assert state_string.meta.id == "a517d519-e326-4690-076e-115f6c632da6"
    assert state_string.meta.type == "state"
    assert state_string.meta.version == "2.1"
    assert state_string.meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"
    assert state_string.meta.manufacturer == "d510770c-e8cc-4b9f-8863-6044b96bb799"
    assert state_string.meta.created == datetime.strptime(
        "2022-09-14T18:39:45.340401Z", TIMESTAMP_FORMAT
    )
    assert state_string.meta.updated == datetime.strptime(
        "2022-10-15T16:29:17.112739Z", TIMESTAMP_FORMAT
    )
    assert not state_string.meta.tag
    assert not state_string.meta.tag_by_user
    assert state_string.meta.name_by_user == "Report"
    assert state_string.meta.iot is True


def test_state_number_obj(state_number_obj):
    """Test state number from dict"""
    state_number = State.from_dict(state_number_obj)
    assert state_number.timestamp == datetime.strptime(
        "2022-10-15T16:29:15.764136Z", TIMESTAMP_FORMAT
    )
    assert state_number.data == 0
    assert state_number.status_payment == "owned"
    assert state_number.type == "Control"
    assert state_number.meta.id == "69d1f4fa-b664-46f2-321e-db6a7dc12776"
    assert state_number.meta.type == "state"
    assert state_number.meta.version == "2.1"
    assert state_number.meta.owner == "a4e0a961-b3f5-4571-8a68-30cbb140d204"
    assert state_number.meta.manufacturer == "d510770c-e8cc-4b9f-8863-6044b96bb799"
    assert state_number.meta.created == datetime.strptime(
        "2022-09-14T18:39:45.340401Z", TIMESTAMP_FORMAT
    )
    assert state_number.meta.updated == datetime.strptime(
        "2022-10-15T16:29:15.987863Z", TIMESTAMP_FORMAT
    )
    assert not state_number.meta.tag
    assert not state_number.meta.tag_by_user
    assert state_number.meta.name_by_user == "Control"
    assert state_number.meta.iot is True

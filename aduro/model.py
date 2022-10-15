"""Data classes for Aduro"""
from dataclasses import dataclass
from datetime import datetime
from typing import Any, cast

from .helpers import try_convert_object


@dataclass
class Connection:
    """Dataclass for device connection"""

    timestamp: datetime
    online: bool

    @staticmethod
    def from_dict(obj: Any) -> "Connection":
        """Create Connection from dict"""
        _timestamp = datetime.strptime(obj.get("timestamp"), "%Y-%m-%dT%H:%M:%S.%fZ")
        _online = obj.get("online")
        return Connection(timestamp=_timestamp, online=_online)


# pylint: disable=too-many-instance-attributes
@dataclass
class Meta:
    """Meta class for device meta"""

    id: str  # pylint: disable=C0103
    type: str
    version: str
    owner: str
    manufacturer: str
    created: datetime
    updated: datetime
    tag: [object]
    tag_by_user: [object]
    name_by_user: str
    iot: bool
    connection: Connection | None
    stable_connection: Connection | None

    @staticmethod
    def from_dict(obj: Any) -> "Meta":
        """Converts a dict to a Meta object"""
        _id = str(obj.get("id"))
        _type = str(obj.get("type"))
        _version = str(obj.get("version"))
        _owner = str(obj.get("owner"))
        _manufacturer = str(obj.get("manufacturer"))
        _created = datetime.strptime(obj.get("created"), "%Y-%m-%dT%H:%M:%S.%fZ")
        _updated = datetime.strptime(obj.get("updated"), "%Y-%m-%dT%H:%M:%S.%fZ")
        _tag = list(obj.get("tag"))
        _tag_by_user = list(obj.get("tag_by_user"))
        _name_by_user = str(obj.get("name_by_user"))
        _iot = bool(obj.get("iot"))
        _connection = (
            Connection.from_dict(obj.get("connection")) if "connection" in obj.keys() else None
        )
        _stable_connection = (
            Connection.from_dict(obj.get("stable_connection"))
            if "stable_connection" in obj.keys()
            else None
        )
        return Meta(
            _id,
            _type,
            _version,
            _owner,
            _manufacturer,
            _created,
            _updated,
            _tag,
            _tag_by_user,
            _name_by_user,
            _iot,
            _connection,
            _stable_connection,
        )


# pylint: enable=too-many-instance-attributes


@dataclass
class Device:
    """Device class"""

    status: [object]
    value: [str]
    name: str
    manufacturer: str
    product: str
    version: str
    serial: str
    description: str
    protocol: str
    communication: str
    meta: Meta

    @staticmethod
    def from_dict(obj: Any) -> "Device":
        """Converts a dict to a Device object"""
        _status = obj.get("status")
        _value = obj.get("value")
        _name = str(obj.get("name"))
        _manufacturer = str(obj.get("manufacturer"))
        _product = str(obj.get("product"))
        _version = str(obj.get("version"))
        _serial = str(obj.get("serial"))
        _description = str(obj.get("description"))
        _protocol = str(obj.get("protocol"))
        _communication = str(obj.get("communication"))
        _meta = Meta.from_dict(obj.get("meta"))
        return Device(
            _status,
            _value,
            _name,
            _manufacturer,
            _product,
            _version,
            _serial,
            _description,
            _protocol,
            _communication,
            _meta,
        )


@dataclass
class Number:
    """Number class for device numbers"""

    min: float
    max: float
    step: float
    unit: str

    @staticmethod
    def from_dict(obj: Any) -> "Number":
        """Converts a dict to a Number object"""
        _min = float(obj.get("min"))
        _max = float(obj.get("max"))
        _step = float(obj.get("step"))
        _unit = str(obj.get("unit"))
        return Number(_min, _max, _step, _unit)


@dataclass
class String:
    """String class for device strings"""

    max: int
    encoding: str

    @staticmethod
    def from_dict(obj: Any) -> "String":
        """Converts a dict to a String object"""
        _max = int(obj.get("max"))
        _encoding = str(obj.get("encoding"))
        return String(_max, _encoding)


@dataclass
class Entity:
    """Entity class for device entitie"""

    state: [str]
    eventlog: [object]
    name: str
    type: str
    period: str
    delta: str
    permission: str
    number: Number | None
    string: String | None
    meta: Meta

    @staticmethod
    def from_dict(obj: Any) -> "Entity":
        """Converts a dict to a Entity object"""
        _state = list(obj.get("state"))
        _eventlog = list(obj.get("eventlog"))
        _name = str(obj.get("name"))
        _type = str(obj.get("type"))
        _period = str(obj.get("period"))
        _delta = str(obj.get("delta"))
        _permission = str(obj.get("permission"))
        _number = Number.from_dict(obj.get("number")) if "number" in obj.keys() else None
        _string = String.from_dict(obj.get("string")) if "string" in obj.keys() else None
        _meta = Meta.from_dict(obj.get("meta"))
        return Entity(
            _state,
            _eventlog,
            _name,
            _type,
            _period,
            _delta,
            _permission,
            _number,
            _string,
            _meta,
        )


@dataclass
class State:
    """State class for device entity state"""

    timestamp: datetime
    data: Any
    status_payment: str
    type: str
    meta: Meta

    @staticmethod
    def from_dict(obj: Any) -> "State":
        """Converts a dict to a State object"""
        _timestamp = datetime.strptime(obj.get("timestamp"), "%Y-%m-%dT%H:%M:%S.%fZ")
        _value = try_convert_object(obj, "data")
        _status_payment = str(obj.get("status_payment"))
        _type = str(obj.get("type"))
        _meta = Meta.from_dict(obj.get("meta"))
        return State(
            _timestamp,
            _value,
            _status_payment,
            _type,
            _meta,
        )

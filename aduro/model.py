"""Data classes for Aduro"""

from datetime import datetime
from typing import Any, List

# pylint: disable=import-error
from pydantic import Field
from pydantic.dataclasses import dataclass

# pylint: enable=import-error


@dataclass
class Connection:
    """Dataclass for device connection"""

    timestamp: datetime
    online: bool = False


# pylint: disable=too-many-instance-attributes
@dataclass
class Meta:
    """Meta class for device meta"""

    id: str  # pylint: disable = invalid-name
    type: str
    version: str
    owner: str
    manufacturer: str
    created: datetime
    updated: datetime
    tag: List[object]
    tag_by_user: List[object]
    name_by_user: str
    iot: bool = Field(default=None)
    connection: Connection = Field(default=None)
    stable_connection: Connection = Field(default=None)


@dataclass
class Device:
    """Device class"""

    status: List[object]
    value: List[str]
    name: str
    manufacturer: str
    product: str
    version: str
    serial: str
    description: str
    protocol: str
    communication: str
    meta: Meta


# pylint: enable=too-many-instance-attributes


@dataclass
class Number:
    """Number class for device numbers"""

    min: float
    max: float
    step: float
    unit: str


@dataclass
class String:
    """String class for device strings"""

    max: int
    encoding: str


# pylint: disable=too-many-instance-attributes
@dataclass
class Entity:
    """Entity class for device entitie"""

    state: List[str]
    eventlog: List[object]
    name: str
    type: str
    period: str
    delta: str
    permission: str
    number: Number = Field(default=None)
    string: String = Field(default=None)
    meta: Meta = Field(default=None)


# pylint: enable=too-many-instance-attributes


@dataclass
class State:
    """State class for device entity state"""

    timestamp: datetime
    data: Any
    status_payment: str
    type: str
    meta: Meta

"""Encode datetime in json"""
import json
from datetime import datetime


class DateTimeEncoder(json.JSONEncoder):
    """datetime encoder class"""

    def default(self, o):
        """overwrites default method"""
        if isinstance(o, datetime):
            return o.isoformat(timespec="seconds")

        return json.JSONEncoder.default(self, o)

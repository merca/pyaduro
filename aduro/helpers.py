"""Helper methods for the Seluxit API."""
from typing import Any


def try_convert_object(obj: Any, field_name: str) -> Any:
    """Try convert the object to the correct value."""
    orig_value = obj.get(field_name)
    try:
        if "." in orig_value:
            value = float(orig_value)
            return value
        raise ValueError
    except ValueError:
        try:
            value = int(orig_value)
            return value
        except ValueError as err:
            try:
                if orig_value == "true":
                    return True
                if orig_value == "false":
                    return False
                raise ValueError from err
            except ValueError:
                return str(orig_value)

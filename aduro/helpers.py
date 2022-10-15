"""Helper methods for the Seluxit API."""
from typing import Any


def try_convert_object(obj: Any, field_name: str) -> Any:
    """Try convert the object to the correct value."""
    if obj.get(field_name) is None:
        return None
    try:
        orig_value = obj.get(field_name)
        if "." in orig_value:
            return float(obj.get(field_name))
        raise ValueError
    except ValueError:
        try:
            return int(obj.get(field_name))
        except ValueError as err:
            try:
                orig_value = obj.get(field_name)
                if orig_value == "true":
                    return True
                if orig_value == "false":
                    return False
                raise ValueError from err
            except ValueError:
                value = str(obj.get(field_name))
                return value

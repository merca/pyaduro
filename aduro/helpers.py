"""Helper methods for the Seluxit API."""
from typing import Any, cast


def try_convert_object(obj: Any, field_name: str) -> Any:
    """Try convert the object to the correct value."""
    try:
        orig_value = obj.get(field_name)
        if orig_value is None:
            return None
        if "." in orig_value:
            value = float(obj.get(field_name))
            return value
        raise ValueError
    except ValueError:
        try:
            value = int(obj.get(field_name))
            return value
        except ValueError:
            try:
                orig_value = obj.get(field_name)
                if orig_value is None:
                    return None
                if orig_value == "true":
                    return True
                if orig_value == "false":
                    return False
                raise ValueError
            except ValueError:
                value = str(obj.get(field_name))
                return value

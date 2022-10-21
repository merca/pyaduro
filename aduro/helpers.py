"""Helper methods for the Seluxit API."""
from typing import Any, Union


def try_convert_object(obj: Any, field_name: str) -> Union[int, float, bool, str, None]:
    """
        Try convert the object to the correct value.
        It is unused but I keep this when I find out how to get `pydantic` to use custom parser.
    """
    orig_value = obj.get(field_name)
    if orig_value is None:
        return None
    if "." in orig_value:
        value = float(orig_value)
    elif orig_value.lower() == "true":
        value = True
    elif orig_value.lower() == "false":
        value = False
    elif orig_value.isdigit():
        value = int(orig_value)
    else:
        value = str(orig_value)
    return value

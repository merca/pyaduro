"""
Tests for helper methodes
"""
from aduro.helpers import try_convert_object


def test_try_conert_object():
    """Test the try_convert_object method."""
    obj = {"test": "test"}
    assert try_convert_object(obj, "test") == "test"
    obj = {"test": "1"}
    assert try_convert_object(obj, "test") == 1
    obj = {"test": "1.1"}
    assert try_convert_object(obj, "test") == 1.1
    obj = {"test": "true"}
    assert try_convert_object(obj, "test") == True
    obj = {"test": "false"}
    assert try_convert_object(obj, "test") == False

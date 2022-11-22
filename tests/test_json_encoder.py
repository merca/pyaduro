"""Test json encoding of datetime objects."""
import datetime
import json

from aduro.datetime_encoder import DateTimeEncoder


def test_datetime_encoder():
    """Test that the DateTimeEncoder class works as expected."""
    create_date = datetime.datetime(2018, 1, 1, 1, 1, 1, 1)

    assert (
        json.dumps(
            create_date,
            cls=DateTimeEncoder,
        )
        == '"2018-01-01T01:01:01"'
    )


def test_datetime_encoder_with_timezone():
    """Test that the DateTimeEncoder class works as expected."""
    create_date = datetime.datetime(
        2018,
        1,
        1,
        1,
        1,
        1,
        1,
        tzinfo=datetime.timezone.utc,
    )

    assert (
        json.dumps(
            create_date,
            cls=DateTimeEncoder,
        )
        == '"2018-01-01T01:01:01+00:00"'
    )


def test_datetime_encoder_with_int_type():
    """Test that the DateTimeEncoder class works as expected."""

    assert (
        json.dumps(
            1514766461,
            cls=DateTimeEncoder,
            default=int,
        )
        == "1514766461"
    )

"""
Tests for pyAduro
"""

import aiohttp  # noqa E402 # pylint: disable=import-error
import pytest  # noqa E402 # pylint: disable=import-error

from aduro import Aduro


@pytest.mark.asyncio
async def test_login():
    """Test login"""
    async with aiohttp.ClientSession():
        aduro_client = Aduro()
        with pytest.raises(NotImplementedError):
            await aduro_client.login("username", "password")

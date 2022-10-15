"""
Tests for pyAduro
"""

import aiohttp  # noqa E402
import pytest  # noqa E402

from aduro import Aduro


@pytest.mark.asyncio
async def test_login():
    """Test login"""
    async with aiohttp.ClientSession():
        aduro_client = Aduro()
        with pytest.raises(NotImplementedError):
            await aduro_client.login("username", "password")

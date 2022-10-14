"""
Tests for pyAduro
"""

import aiohttp
import pytest

from pyAduro import Aduro


@pytest.mark.asyncio
async def test_login():
    """Test login"""
    async with aiohttp.ClientSession():
        aduro_client = Aduro()
        with pytest.raises(NotImplementedError):
            await aduro_client.login("username", "password")

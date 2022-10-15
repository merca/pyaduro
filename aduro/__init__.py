"""
Aduro Stove on Seluxit Echidna proxy that communicates via Wappsto API
"""
from .version import __version__

import asyncio


class Aduro:
    """Aduro Stove proxi client"""

    def __init__(self) -> None:
        """Initialize Aduro Stove"""

    async def login(self, username, password) -> None:
        """Login to Aduro Stove

        Args:
            username (_type_): username to Wappsto account
            password (_type_): password to Wappsto account

        Raises:
            NotImplementedError: this is initial version of the library
        """
        raise NotImplementedError

    def make_some_tests_fail(self):
        print(
            "very long line that should be split into multiple lines, and some more text to make black angry"
        )
        name = input("Hello! What is your name?\n")
        print(
            "Well, {0}, I am thinking of a number between 1 and 20. And something more to make sure its long".format(
                name
            )
        )


import itertools

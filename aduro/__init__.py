"""
Aduro Stove on Seluxit Echidna proxy that communicates via Wappsto API
"""
from .version import __version__


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

    def temporary_to_make_pylint_happy(self):
        """Temporary function"""

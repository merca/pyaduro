"""
    Aduro integration client
"""


class AduroClient:
    """Aduro client class."""

    def __init__(self) -> None:
        """Initialize Aduro Stove client"""

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

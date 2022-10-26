"""Aduro integration client"""


class AduroClient:
    """Aduro client class."""

    def __init__(self) -> None:
        """Initialize Aduro Stove client"""

    async def login(self, username, password) -> None:
        """Login into account with username and password

        :param username: username to Wappsto account
        :type username: _type_
        :param password: password to Wappsto account
        :type password: _type_
        :raises NotImplementedError: Not implemented yet
        """
        raise NotImplementedError

    def temporary_to_make_pylint_happy(self):
        """Temporary function"""

"""
Aduro Stove Wappsto API proxy
"""


class Aduro:
    """Aduro Stove proxy client"""

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

    def __repr__(self) -> str:
        """Representation of Aduro Stove"""
        return f"Aduro Stove version {__version__}"

    def temporary_to_make_pylint_happy(self):
        """Temporary function"""

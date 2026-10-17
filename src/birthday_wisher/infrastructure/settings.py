"""!
@file settings.py
@brief Reads the sender's address and token from the environment.
"""

from collections.abc import Mapping
from dataclasses import dataclass

from birthday_wisher import constants
from birthday_wisher.domain.errors import ConfigurationError


@dataclass(frozen=True)
class Credentials:
    """!
    @brief The sender's login.
    @param address Sender e-mail address.
    @param token Password or app password; hidden from repr.
    """

    address: str
    token: str

    def __repr__(self) -> str:
        return f"Credentials(address={self.address!r}, token='***')"


def read_credentials(environ: Mapping[str, str]) -> Credentials:
    """!
    @brief Read the credentials from an environment mapping.
    @details Only the names of the missing variables are reported, never a value.
    @param environ Environment variables, normally os.environ.
    @return The credentials.
    @throws ConfigurationError when a variable is missing or empty.
    """
    names = (constants.ENV_SENDER_ADDRESS, constants.ENV_SENDER_TOKEN)
    missing = [name for name in names if not environ.get(name)]
    if missing:
        raise ConfigurationError(
            f"missing environment variable(s): {', '.join(missing)}"
        )
    return Credentials(environ[names[0]], environ[names[1]])

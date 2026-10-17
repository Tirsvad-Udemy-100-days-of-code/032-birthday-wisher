"""Tests for reading the sender credentials from an environment mapping."""

import pytest

from birthday_wisher import constants
from birthday_wisher.domain.errors import ConfigurationError
from birthday_wisher.infrastructure.settings import Credentials, read_credentials

ADDRESS = constants.ENV_SENDER_ADDRESS
TOKEN = constants.ENV_SENDER_TOKEN


def test_read_credentials_returns_address_and_token() -> None:
    """Both variables present give the credentials."""
    result = read_credentials({ADDRESS: "me@example.com", TOKEN: "tok"})
    assert result == Credentials("me@example.com", "tok")


def test_read_credentials_reports_missing_names_not_values() -> None:
    """The error names the missing variable and shows no value."""
    with pytest.raises(ConfigurationError) as info:
        read_credentials({ADDRESS: "me@example.com"})
    text = str(info.value)
    assert TOKEN in text
    assert "me@example.com" not in text


def test_read_credentials_reports_both_when_none_set() -> None:
    """Both missing names are listed."""
    with pytest.raises(ConfigurationError) as info:
        read_credentials({})
    assert ADDRESS in str(info.value)
    assert TOKEN in str(info.value)


def test_read_credentials_treats_empty_value_as_missing() -> None:
    """An empty value counts as missing."""
    with pytest.raises(ConfigurationError, match=TOKEN):
        read_credentials({ADDRESS: "me@example.com", TOKEN: ""})


def test_credentials_repr_hides_token() -> None:
    """Neither repr nor str shows the token."""
    credentials = Credentials("me@example.com", "super-secret")
    assert "super-secret" not in repr(credentials)
    assert "super-secret" not in str(credentials)

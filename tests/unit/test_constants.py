"""Smoke test: the package imports and the constants are consistent."""

from birthday_wisher import constants


def test_letter_file_pattern_has_number_placeholder() -> None:
    assert "{number}" in constants.LETTER_FILE_PATTERN


def test_csv_columns_start_with_name_and_email() -> None:
    assert constants.CSV_COLUMNS[:2] == ("name", "email")


def test_smtp_port_expects_starttls() -> None:
    assert constants.SMTP_PORT == 587

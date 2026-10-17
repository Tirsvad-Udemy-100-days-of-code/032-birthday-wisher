"""Integration tests for CsvBirthdayRepository against real files."""

from pathlib import Path

import pytest

from birthday_wisher.domain.errors import BirthdayDataError
from birthday_wisher.domain.person import Person
from birthday_wisher.infrastructure.csv_birthday_repository import (
    CsvBirthdayRepository,
)

HEADER = "name,email,year,month,day\n"


def _write(tmp_path: Path, text: str) -> Path:
    path = tmp_path / "birthdays.csv"
    path.write_text(text, encoding="utf-8")
    return path


def test_load_all_reads_people_in_file_order(tmp_path: Path) -> None:
    """Rows become Person objects in file order."""
    path = _write(
        tmp_path,
        HEADER + "Ann,ann@example.com,1990,3,14\nBob,bob@example.com,1985,10,17\n",
    )
    assert CsvBirthdayRepository(path).load_all() == [
        Person("Ann", "ann@example.com", 1990, 3, 14),
        Person("Bob", "bob@example.com", 1985, 10, 17),
    ]


def test_load_all_header_only_gives_empty_list(tmp_path: Path) -> None:
    """A file with only a header holds nobody."""
    assert CsvBirthdayRepository(_write(tmp_path, HEADER)).load_all() == []


def test_load_all_missing_file_raises(tmp_path: Path) -> None:
    """A missing file raises BirthdayDataError."""
    with pytest.raises(BirthdayDataError):
        CsvBirthdayRepository(tmp_path / "nope.csv").load_all()


def test_load_all_missing_column_raises(tmp_path: Path) -> None:
    """A missing column is named in the error."""
    path = _write(tmp_path, "name,email,year,month\nAnn,a@example.com,1990,3\n")
    with pytest.raises(BirthdayDataError, match="day"):
        CsvBirthdayRepository(path).load_all()


def test_load_all_non_numeric_value_raises(tmp_path: Path) -> None:
    """A non-numeric month raises and names the line."""
    path = _write(tmp_path, HEADER + "Ann,a@example.com,1990,March,14\n")
    with pytest.raises(BirthdayDataError, match="line 2"):
        CsvBirthdayRepository(path).load_all()


def test_load_all_short_row_raises(tmp_path: Path) -> None:
    """A row with too few fields raises BirthdayDataError."""
    path = _write(tmp_path, HEADER + "Ann,a@example.com,1990\n")
    with pytest.raises(BirthdayDataError):
        CsvBirthdayRepository(path).load_all()

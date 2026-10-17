"""!
@file csv_birthday_repository.py
@brief Reads the people from the birthdays CSV file.
"""

import csv
from pathlib import Path

from birthday_wisher import constants
from birthday_wisher.domain.errors import BirthdayDataError
from birthday_wisher.domain.person import Person


class CsvBirthdayRepository:
    """!
    @brief BirthdayRepository backed by a CSV file with the columns of CSV_COLUMNS.
    @param path Path of the CSV file.
    """

    def __init__(self, path: Path) -> None:
        self._path = path

    def load_all(self) -> list[Person]:
        """!
        @brief Read every row of the file.
        @return All people, in file order.
        @throws BirthdayDataError when the file is missing or a row is invalid.
        """
        try:
            with self._path.open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                missing = set(constants.CSV_COLUMNS) - set(reader.fieldnames or [])
                if missing:
                    raise BirthdayDataError(
                        f"{self._path}: missing column(s) {sorted(missing)}"
                    )
                return [
                    self._to_person(row, number)
                    for number, row in enumerate(reader, start=2)
                ]
        except OSError as err:
            raise BirthdayDataError(f"cannot read {self._path}: {err}") from err

    def _to_person(self, row: dict[str, str], line: int) -> Person:
        try:
            return Person(
                name=row["name"].strip(),
                email=row["email"].strip(),
                year=int(row["year"]),
                month=int(row["month"]),
                day=int(row["day"]),
            )
        except (TypeError, ValueError, AttributeError) as err:
            raise BirthdayDataError(f"{self._path} line {line}: invalid row") from err

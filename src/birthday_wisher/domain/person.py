"""!
@file person.py
@brief The Person entity: a name, an e-mail address and a birth date.
"""

import calendar
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Person:
    """!
    @brief A person who should receive a birthday wish.
    @param name Name that replaces the placeholder in the letter.
    @param email Address the letter is sent to.
    @param year Year of birth.
    @param month Month of birth (1 to 12).
    @param day Day of birth (1 to 31).
    """

    name: str
    email: str
    year: int
    month: int
    day: int

    @property
    def birthday(self) -> tuple[int, int]:
        """!
        @brief The (month, day) pair the course hints use as dictionary key.
        @return Tuple of month and day of birth.
        """
        return (self.month, self.day)

    def has_birthday_on(self, today: date) -> bool:
        """!
        @brief Tell whether the given day is this person's birthday.
        @details A birthday on 29 February is celebrated on 28 February in
        years that are not leap years.
        @param today The day to check.
        @return True when month and day match.
        """
        if self.birthday == (2, 29) and not calendar.isleap(today.year):
            return (today.month, today.day) == (2, 28)
        return (today.month, today.day) == self.birthday

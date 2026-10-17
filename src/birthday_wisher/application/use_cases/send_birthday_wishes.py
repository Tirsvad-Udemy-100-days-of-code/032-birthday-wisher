"""!
@file send_birthday_wishes.py
@brief Use case: send a random birthday letter to everyone whose birthday is today.
"""

from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import date

from birthday_wisher import constants
from birthday_wisher.application.ports import (
    BirthdayRepository,
    LetterSource,
    MailSender,
)
from birthday_wisher.domain.errors import MailError
from birthday_wisher.domain.person import Person


@dataclass
class WishReport:
    """!
    @brief Outcome of one run.
    @param sent Names of the people who were sent a letter.
    @param failed Names of the people whose letter could not be sent.
    """

    sent: list[str] = field(default_factory=list)
    failed: list[str] = field(default_factory=list)


def birthdays_by_day(people: list[Person]) -> dict[tuple[int, int], list[Person]]:
    """!
    @brief Build the dictionary the course hints describe.
    @details The key is (month, day). The value is a list, because two people
    can share a birthday.
    @param people All people.
    @return Mapping from (month, day) to the people born on that day.
    """
    result: dict[tuple[int, int], list[Person]] = {}
    for person in people:
        result.setdefault(person.birthday, []).append(person)
    return result


def find_birthday_people(people: list[Person], today: date) -> list[Person]:
    """!
    @brief Select the people whose birthday is on the given day.
    @param people All people.
    @param today The day to check.
    @return The people to wish a happy birthday, in file order.
    """
    return [person for person in people if person.has_birthday_on(today)]


def build_letter(template: str, name: str) -> str:
    """!
    @brief Put the person's name into a letter template.
    @param template Template text containing the name placeholder.
    @param name Name of the recipient.
    @return The finished letter.
    """
    return template.replace(constants.NAME_PLACEHOLDER, name)


def send_birthday_wishes(
    repository: BirthdayRepository,
    letters: LetterSource,
    mailer: MailSender,
    today: date,
    choose_letter: Callable[[], int],
) -> WishReport:
    """!
    @brief Send one random letter to everyone whose birthday is today.
    @param repository Source of the people.
    @param letters Source of the letter templates.
    @param mailer Sends the e-mail.
    @param today The day to check.
    @param choose_letter Returns the number of the template to use (1 to LETTER_COUNT).
    @return Who was sent a letter and for whom sending failed.
    """
    report = WishReport()
    for person in find_birthday_people(repository.load_all(), today):
        body = build_letter(letters.read_letter(choose_letter()), person.name)
        try:
            mailer.send(person.email, constants.EMAIL_SUBJECT, body)
        except MailError:
            report.failed.append(person.name)
        else:
            report.sent.append(person.name)
    return report

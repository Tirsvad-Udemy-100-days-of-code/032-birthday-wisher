"""Unit tests for the send-birthday-wishes use case, using fakes of the ports."""

from datetime import date

from birthday_wisher import constants
from birthday_wisher.application.use_cases.send_birthday_wishes import (
    birthdays_by_day,
    build_letter,
    find_birthday_people,
    send_birthday_wishes,
)
from birthday_wisher.domain.errors import MailError
from birthday_wisher.domain.person import Person

TODAY = date(2026, 10, 17)
ALICE = Person("Alice", "alice@example.com", 1990, 3, 14)
BOB = Person("Bob", "bob@example.com", 1985, 10, 17)
CAROL = Person("Carol", "carol@example.com", 2001, 10, 17)


class FakeRepository:
    """In-memory BirthdayRepository."""

    def __init__(self, people: list[Person]) -> None:
        self._people = people

    def load_all(self) -> list[Person]:
        return list(self._people)


class FakeLetters:
    """In-memory LetterSource."""

    def read_letter(self, number: int) -> str:
        return f"Letter {number} for [NAME]"


class FakeMailer:
    """Records mails; fails for the addresses in `fail_for`."""

    def __init__(self, fail_for: set[str] | None = None) -> None:
        self.sent: list[tuple[str, str, str]] = []
        self._fail_for = fail_for or set()

    def send(self, recipient: str, subject: str, body: str) -> None:
        if recipient in self._fail_for:
            raise MailError("boom")
        self.sent.append((recipient, subject, body))


def test_find_birthday_people_selects_only_today() -> None:
    assert find_birthday_people([ALICE, BOB], TODAY) == [BOB]


def test_find_birthday_people_returns_both_sharing_a_day() -> None:
    assert find_birthday_people([BOB, ALICE, CAROL], TODAY) == [BOB, CAROL]


def test_find_birthday_people_empty_when_nobody() -> None:
    assert find_birthday_people([ALICE], TODAY) == []


def test_birthdays_by_day_groups_people_sharing_a_day() -> None:
    result = birthdays_by_day([ALICE, BOB, CAROL])
    assert result == {(3, 14): [ALICE], (10, 17): [BOB, CAROL]}


def test_build_letter_replaces_name() -> None:
    assert build_letter("Dear [NAME],", "Bob") == "Dear Bob,"


def test_build_letter_replaces_every_placeholder() -> None:
    assert build_letter("[NAME] and [NAME]", "Bo") == "Bo and Bo"


def test_send_wishes_sends_one_letter_to_todays_person_only() -> None:
    mailer = FakeMailer()
    report = send_birthday_wishes(
        FakeRepository([ALICE, BOB]), FakeLetters(), mailer, TODAY, lambda: 2
    )
    assert mailer.sent == [
        ("bob@example.com", constants.EMAIL_SUBJECT, "Letter 2 for Bob")
    ]
    assert report.sent == ["Bob"]
    assert report.failed == []


def test_send_wishes_with_no_birthday_sends_nothing() -> None:
    mailer = FakeMailer()
    report = send_birthday_wishes(
        FakeRepository([ALICE]), FakeLetters(), mailer, TODAY, lambda: 1
    )
    assert mailer.sent == []
    assert report.sent == [] and report.failed == []


def test_send_wishes_one_failure_does_not_stop_the_others() -> None:
    mailer = FakeMailer(fail_for={"bob@example.com"})
    report = send_birthday_wishes(
        FakeRepository([BOB, CAROL]), FakeLetters(), mailer, TODAY, lambda: 1
    )
    assert report.failed == ["Bob"]
    assert report.sent == ["Carol"]
    assert [m[0] for m in mailer.sent] == ["carol@example.com"]

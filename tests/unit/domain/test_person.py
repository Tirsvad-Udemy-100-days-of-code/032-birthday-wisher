"""Unit tests for the Person entity."""

from datetime import date

from birthday_wisher.domain.person import Person


def _person(month: int, day: int) -> Person:
    return Person("Ann", "ann@example.com", 1990, month, day)


def test_has_birthday_on_same_month_and_day() -> None:
    assert _person(10, 17).has_birthday_on(date(2026, 10, 17))


def test_has_birthday_on_other_day_is_false() -> None:
    assert not _person(10, 17).has_birthday_on(date(2026, 10, 18))


def test_has_birthday_on_same_day_other_month_is_false() -> None:
    assert not _person(10, 17).has_birthday_on(date(2026, 11, 17))


def test_has_birthday_on_ignores_year() -> None:
    assert _person(10, 17).has_birthday_on(date(1999, 10, 17))


def test_leap_day_birthday_is_29_feb_in_leap_year() -> None:
    assert _person(2, 29).has_birthday_on(date(2024, 2, 29))


def test_leap_day_birthday_is_not_28_feb_in_leap_year() -> None:
    assert not _person(2, 29).has_birthday_on(date(2024, 2, 28))


def test_leap_day_birthday_is_28_feb_in_non_leap_year() -> None:
    assert _person(2, 29).has_birthday_on(date(2026, 2, 28))


def test_leap_day_birthday_is_not_1_mar_in_non_leap_year() -> None:
    assert not _person(2, 29).has_birthday_on(date(2026, 3, 1))


def test_28_feb_birthday_is_28_feb_in_non_leap_year() -> None:
    assert _person(2, 28).has_birthday_on(date(2026, 2, 28))

"""End-to-end tests of the command line: real files, fake SMTP, no network."""

import smtplib
from email.message import EmailMessage
from pathlib import Path
from types import TracebackType
from typing import ClassVar, Self

import pytest

from birthday_wisher import constants
from birthday_wisher.presentation.cli import main

ROOT = Path(__file__).resolve().parents[3]
ENV = {
    constants.ENV_SENDER_ADDRESS: "me@example.com",
    constants.ENV_SENDER_TOKEN: "tok-123",
}


class FakeSmtp:
    """Records the messages sent through every instance."""

    messages: ClassVar[list[EmailMessage]] = []
    fail = False

    def __init__(self, host: str, port: int) -> None:
        pass

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        return None

    def starttls(self) -> None:
        return None

    def login(self, user: str, password: str) -> None:
        if FakeSmtp.fail:
            raise smtplib.SMTPAuthenticationError(535, b"no")

    def send_message(self, message: EmailMessage) -> None:
        FakeSmtp.messages.append(message)


@pytest.fixture(autouse=True)
def _reset() -> None:
    FakeSmtp.messages = []
    FakeSmtp.fail = False


@pytest.fixture
def data(tmp_path: Path) -> list[str]:
    """Arguments for a temporary CSV (Bob and Carol on 10-17) and real letters."""
    csv_path = tmp_path / "b.csv"
    csv_path.write_text(
        "name,email,year,month,day\n"
        "Alice,alice@example.com,1990,3,14\n"
        "Bob,bob@example.com,1985,10,17\n"
        "Carol,carol@example.com,2001,10,17\n",
        encoding="utf-8",
    )
    return ["--csv", str(csv_path), "--letters", str(ROOT / "letter_templates")]


def test_dry_run_prints_to_and_subject_without_env(
    data: list[str], capsys: pytest.CaptureFixture[str]
) -> None:
    """Dry run needs no environment and prints finished letters."""
    code = main([*data, "--today", "2026-10-17", "--dry-run"], environ={})
    out = capsys.readouterr().out
    assert code == 0
    assert "To: bob@example.com" in out
    assert "To: carol@example.com" in out
    assert "Subject: Happy Birthday" in out
    assert "[NAME]" not in out
    assert "alice@example.com" not in out


def test_real_mode_sends_through_fake_smtp(
    data: list[str], capsys: pytest.CaptureFixture[str]
) -> None:
    """Real mode sends one mail per birthday person through the factory."""
    code = main([*data, "--today", "2026-10-17"], environ=ENV, smtp_factory=FakeSmtp)
    assert code == 0
    assert sorted(str(m["To"]) for m in FakeSmtp.messages) == [
        "bob@example.com",
        "carol@example.com",
    ]
    assert all(m["Subject"] == "Happy Birthday" for m in FakeSmtp.messages)
    assert "Sent a birthday letter to Bob." in capsys.readouterr().out


def test_missing_env_returns_1_naming_variable_not_value(
    data: list[str], capsys: pytest.CaptureFixture[str]
) -> None:
    """A missing variable is named, its sibling's value is not shown."""
    env = {constants.ENV_SENDER_ADDRESS: "me@example.com"}
    code = main([*data, "--today", "2026-10-17"], environ=env, smtp_factory=FakeSmtp)
    err = capsys.readouterr().err
    assert code == 1
    assert constants.ENV_SENDER_TOKEN in err
    assert "me@example.com" not in err
    assert FakeSmtp.messages == []


def test_no_birthdays_today_prints_message(
    data: list[str], capsys: pytest.CaptureFixture[str]
) -> None:
    """A day without birthdays prints a message and succeeds."""
    code = main([*data, "--today", "2026-01-01", "--dry-run"], environ={})
    assert code == 0
    assert "No birthdays today" in capsys.readouterr().out


def test_missing_csv_returns_1(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """A missing CSV file returns 1 with an error message."""
    code = main(["--csv", str(tmp_path / "none.csv"), "--dry-run"], environ={})
    assert code == 1
    assert "error:" in capsys.readouterr().err


def test_smtp_failure_returns_1_without_token(
    data: list[str], capsys: pytest.CaptureFixture[str]
) -> None:
    """A failing login returns 1 and never prints the token."""
    FakeSmtp.fail = True
    code = main([*data, "--today", "2026-10-17"], environ=ENV, smtp_factory=FakeSmtp)
    err = capsys.readouterr().err
    assert code == 1
    assert "tok-123" not in err


def test_shipped_birthdays_csv_has_bob_and_carol_on_oct_17(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """The shipped sample data works with the shipped letters."""
    args = [
        "--csv",
        str(ROOT / "birthdays.csv"),
        "--letters",
        str(ROOT / "letter_templates"),
        "--today",
        "2026-10-17",
        "--dry-run",
    ]
    assert main(args, environ={}) == 0
    out = capsys.readouterr().out
    assert "bob@example.com" in out
    assert "carol@example.com" in out

"""Tests for SmtpMailer with a fake SMTP connection (no network)."""

import smtplib
from email.message import EmailMessage
from types import TracebackType
from typing import ClassVar, Self

import pytest

from birthday_wisher import constants
from birthday_wisher.domain.errors import MailError
from birthday_wisher.infrastructure.smtp_mailer import SmtpMailer

TOKEN = "s3cret-token"


class FakeSmtp:
    """Records calls in order; can raise on a chosen step."""

    calls: ClassVar[list[str]] = []
    messages: ClassVar[list[EmailMessage]] = []
    fail_on: ClassVar[dict[str, Exception]] = {}
    created_with: ClassVar[list[tuple[str, int]]] = []

    def __init__(self, host: str, port: int) -> None:
        FakeSmtp.created_with.append((host, port))

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        FakeSmtp.calls.append("quit")

    def _step(self, name: str) -> None:
        FakeSmtp.calls.append(name)
        if name in FakeSmtp.fail_on:
            raise FakeSmtp.fail_on[name]

    def starttls(self) -> None:
        self._step("starttls")

    def login(self, user: str, password: str) -> None:
        self._step("login")
        assert (user, password) == ("me@example.com", TOKEN)

    def send_message(self, message: EmailMessage) -> None:
        self._step("send_message")
        FakeSmtp.messages.append(message)


@pytest.fixture(autouse=True)
def _reset_fake() -> None:
    FakeSmtp.calls = []
    FakeSmtp.messages = []
    FakeSmtp.fail_on = {}
    FakeSmtp.created_with = []


def _mailer() -> SmtpMailer:
    return SmtpMailer("smtp.test", 587, "me@example.com", TOKEN, FakeSmtp)


def test_send_calls_starttls_then_login_then_send_message() -> None:
    """The SMTP steps run in the required order."""
    _mailer().send("bob@example.com", constants.EMAIL_SUBJECT, "Hi Bob")
    assert FakeSmtp.calls == ["starttls", "login", "send_message", "quit"]
    assert FakeSmtp.created_with == [("smtp.test", 587)]


def test_send_builds_message_with_subject_recipient_and_body() -> None:
    """Subject, recipient, sender and body reach the server."""
    _mailer().send("bob@example.com", constants.EMAIL_SUBJECT, "Hi Bob")
    message = FakeSmtp.messages[0]
    assert message["Subject"] == "Happy Birthday"
    assert message["To"] == "bob@example.com"
    assert message["From"] == "me@example.com"
    assert message.get_content().strip() == "Hi Bob"


@pytest.mark.parametrize("step", ["starttls", "login", "send_message"])
@pytest.mark.parametrize(
    "error",
    [
        smtplib.SMTPAuthenticationError(535, b"bad " + TOKEN.encode()),
        smtplib.SMTPException("x"),
        OSError("net down " + TOKEN),
    ],
)
def test_send_failure_becomes_mail_error_without_token(
    step: str, error: Exception
) -> None:
    """smtplib and OS errors become MailError and never carry the token."""
    FakeSmtp.fail_on = {step: error}
    with pytest.raises(MailError) as info:
        _mailer().send("bob@example.com", "Happy Birthday", "Hi")
    assert TOKEN not in str(info.value)
    assert "bob@example.com" in str(info.value)


def test_send_connection_failure_becomes_mail_error() -> None:
    """A refused connection becomes MailError."""

    def refuse(host: str, port: int) -> FakeSmtp:
        raise ConnectionRefusedError("refused")

    mailer = SmtpMailer("h", 587, "me@example.com", TOKEN, refuse)
    with pytest.raises(MailError):
        mailer.send("bob@example.com", "Happy Birthday", "Hi")

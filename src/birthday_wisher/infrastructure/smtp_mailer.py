"""!
@file smtp_mailer.py
@brief Sends e-mail through an SMTP server with STARTTLS.
"""

import smtplib
from collections.abc import Callable
from email.message import EmailMessage
from typing import Any  # Any: smtplib.SMTP and test fakes share no common type

from birthday_wisher.domain.errors import MailError


class SmtpMailer:
    """!
    @brief MailSender that talks SMTP with STARTTLS.
    @param host SMTP server name.
    @param port SMTP port that expects STARTTLS.
    @param address Sender address, also used to log in.
    @param token Password or app password. Never logged or shown.
    @param smtp_factory Creates the SMTP connection; tests replace it with a fake.
    """

    def __init__(
        self,
        host: str,
        port: int,
        address: str,
        token: str,
        smtp_factory: Callable[[str, int], Any] = smtplib.SMTP,
    ) -> None:
        self._host = host
        self._port = port
        self._address = address
        self._token = token
        self._smtp_factory = smtp_factory

    def send(self, recipient: str, subject: str, body: str) -> None:
        """!
        @brief Connect, start TLS, log in and send one plain-text e-mail.
        @param recipient Address to send to.
        @param subject Subject line.
        @param body Message text.
        @throws MailError when the connection, login or sending fails.
        """
        message = EmailMessage()
        message["From"] = self._address
        message["To"] = recipient
        message["Subject"] = subject
        message.set_content(body)
        try:
            with self._smtp_factory(self._host, self._port) as connection:
                connection.starttls()
                connection.login(self._address, self._token)
                connection.send_message(message)
        except (smtplib.SMTPException, OSError) as err:
            raise MailError(
                f"could not send to {recipient}: {type(err).__name__}"
            ) from err

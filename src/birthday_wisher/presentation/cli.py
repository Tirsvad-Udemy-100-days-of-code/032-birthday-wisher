"""!
@file cli.py
@brief Command line entry point and composition root.
"""

import argparse
import os
import random
import sys
from collections.abc import Callable, Mapping, Sequence
from datetime import date
from pathlib import Path
from typing import Any  # Any: smtplib.SMTP and test fakes share no common type

from birthday_wisher import constants
from birthday_wisher.application.ports import MailSender
from birthday_wisher.application.use_cases.send_birthday_wishes import (
    send_birthday_wishes,
)
from birthday_wisher.domain.errors import BirthdayWisherError
from birthday_wisher.infrastructure.csv_birthday_repository import (
    CsvBirthdayRepository,
)
from birthday_wisher.infrastructure.letter_templates import FolderLetterSource
from birthday_wisher.infrastructure.settings import read_credentials
from birthday_wisher.infrastructure.smtp_mailer import SmtpMailer


class _DryRunMailer:
    """!
    @brief MailSender that prints the e-mail instead of sending it.
    """

    def send(self, recipient: str, subject: str, body: str) -> None:
        """!
        @brief Print the e-mail.
        @param recipient Address the e-mail would go to.
        @param subject Subject line.
        @param body Message text.
        """
        print(f"[dry run] To: {recipient}\nSubject: {subject}\n\n{body}\n")


def build_parser() -> argparse.ArgumentParser:
    """!
    @brief Create the argument parser.
    @return The parser with --dry-run, --today, --csv and --letters.
    """
    parser = argparse.ArgumentParser(
        prog="birthday-wisher",
        description="Send a random birthday letter to everyone born on today's date.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the e-mails instead of sending them",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="pretend today is YYYY-MM-DD",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=Path(constants.BIRTHDAYS_FILE),
        help="birthdays CSV file",
    )
    parser.add_argument(
        "--letters",
        type=Path,
        default=Path(constants.LETTER_TEMPLATES_DIR),
        help="folder with the letter templates",
    )
    return parser


def _choose_letter() -> int:
    return random.randint(1, constants.LETTER_COUNT)


def main(
    argv: Sequence[str] | None = None,
    environ: Mapping[str, str] | None = None,
    smtp_factory: Callable[[str, int], Any] | None = None,
) -> int:
    """!
    @brief Run the program.
    @param argv Command line arguments; sys.argv is used when None.
    @param environ Environment variables; os.environ is used when None.
    @param smtp_factory Creates the SMTP connection; tests pass a fake.
    @return Exit status: 0 on success, 1 when a letter failed or setup is wrong.
    """
    args = build_parser().parse_args(argv)
    env = os.environ if environ is None else environ
    today = args.today or date.today()
    try:
        mailer: MailSender
        if args.dry_run:
            mailer = _DryRunMailer()
        else:
            credentials = read_credentials(env)
            mailer = SmtpMailer(
                constants.SMTP_HOST,
                constants.SMTP_PORT,
                credentials.address,
                credentials.token,
                **({} if smtp_factory is None else {"smtp_factory": smtp_factory}),
            )
        report = send_birthday_wishes(
            CsvBirthdayRepository(args.csv),
            FolderLetterSource(args.letters),
            mailer,
            today,
            _choose_letter,
        )
    except BirthdayWisherError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    if not report.sent and not report.failed:
        print(f"No birthdays today ({today.isoformat()}).")
    for name in report.sent:
        print(f"Sent a birthday letter to {name}.")
    for name in report.failed:
        print(f"error: could not send a letter to {name}.", file=sys.stderr)
    return 1 if report.failed else 0

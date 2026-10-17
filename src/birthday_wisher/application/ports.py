"""!
@file ports.py
@brief Ports: what the use case needs from the outside world.
"""

from typing import Protocol

from birthday_wisher.domain.person import Person


class BirthdayRepository(Protocol):
    """!
    @brief Source of the people and their birth dates.
    """

    def load_all(self) -> list[Person]:
        """!
        @brief Read every person.
        @return All people, in file order.
        """
        ...


class LetterSource(Protocol):
    """!
    @brief Source of the letter templates.
    """

    def read_letter(self, number: int) -> str:
        """!
        @brief Read one template.
        @param number Template number, 1 to LETTER_COUNT.
        @return The template text with its placeholder.
        """
        ...


class MailSender(Protocol):
    """!
    @brief Sends one e-mail.
    """

    def send(self, recipient: str, subject: str, body: str) -> None:
        """!
        @brief Send a plain-text e-mail.
        @param recipient Address to send to.
        @param subject Subject line.
        @param body Message text.
        @throws MailError when the mail cannot be sent.
        """
        ...

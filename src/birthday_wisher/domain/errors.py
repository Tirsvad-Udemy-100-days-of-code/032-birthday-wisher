"""!
@file errors.py
@brief Errors the birthday wisher raises.
"""


class BirthdayWisherError(Exception):
    """!
    @brief Base class of every error raised by this program.
    """


class BirthdayDataError(BirthdayWisherError):
    """!
    @brief The birthdays file is missing or a row in it is invalid.
    """


class LetterTemplateError(BirthdayWisherError):
    """!
    @brief A letter template is missing or unreadable.
    """


class ConfigurationError(BirthdayWisherError):
    """!
    @brief A required setting (sender address or token) is missing.
    """


class MailError(BirthdayWisherError):
    """!
    @brief A letter could not be sent.
    """

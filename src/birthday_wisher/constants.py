"""!
@file constants.py
@brief Constants of the birthday wisher: file names, placeholder, SMTP settings.
"""

## Name of the CSV file with the people and their birth dates.
BIRTHDAYS_FILE: str = "birthdays.csv"

## Folder with the letter templates.
LETTER_TEMPLATES_DIR: str = "letter_templates"

## File name pattern of a letter template (the number is 1 to LETTER_COUNT).
LETTER_FILE_PATTERN: str = "letter_{number}.txt"

## Number of letter templates the program chooses from.
LETTER_COUNT: int = 3

## Placeholder in a letter that is replaced by the person's name.
NAME_PLACEHOLDER: str = "[NAME]"

## Columns of the CSV file.
CSV_COLUMNS: tuple[str, ...] = ("name", "email", "year", "month", "day")

## SMTP server of Gmail.
SMTP_HOST: str = "smtp.gmail.com"

## SMTP port that expects STARTTLS.
SMTP_PORT: int = 587

## Subject of the e-mail.
EMAIL_SUBJECT: str = "Happy Birthday"

## Environment variable with the sender's e-mail address.
ENV_SENDER_ADDRESS: str = "GMAIL_ADDRESS"

## Environment variable with the sender's app password (token).
ENV_SENDER_TOKEN: str = "GMAIL_TOKEN"

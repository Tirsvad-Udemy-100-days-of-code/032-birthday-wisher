"""!
@file letter_templates.py
@brief Reads the letter templates from a folder.
"""

from pathlib import Path

from birthday_wisher import constants
from birthday_wisher.domain.errors import LetterTemplateError


class FolderLetterSource:
    """!
    @brief LetterSource backed by the files letter_1.txt, letter_2.txt, and so on.
    @param folder Folder that holds the templates.
    """

    def __init__(self, folder: Path) -> None:
        self._folder = folder

    def read_letter(self, number: int) -> str:
        """!
        @brief Read one template.
        @param number Template number, 1 to LETTER_COUNT.
        @return The template text.
        @throws LetterTemplateError when the file cannot be read.
        """
        path = self._folder / constants.LETTER_FILE_PATTERN.format(number=number)
        try:
            return path.read_text(encoding="utf-8")
        except OSError as err:
            raise LetterTemplateError(
                f"cannot read letter template {path}: {err}"
            ) from err

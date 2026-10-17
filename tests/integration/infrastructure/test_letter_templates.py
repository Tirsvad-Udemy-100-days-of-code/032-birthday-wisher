"""Integration tests for FolderLetterSource against real files."""

from pathlib import Path

import pytest

from birthday_wisher import constants
from birthday_wisher.application.use_cases.send_birthday_wishes import build_letter
from birthday_wisher.domain.errors import LetterTemplateError
from birthday_wisher.infrastructure.letter_templates import FolderLetterSource

LETTERS_DIR = Path(__file__).resolve().parents[3] / constants.LETTER_TEMPLATES_DIR


@pytest.mark.parametrize("number", range(1, constants.LETTER_COUNT + 1))
def test_every_real_template_can_be_chosen_and_built(number: int) -> None:
    """Each shipped template holds the placeholder and is fully replaced."""
    template = FolderLetterSource(LETTERS_DIR).read_letter(number)
    assert constants.NAME_PLACEHOLDER in template
    letter = build_letter(template, "Zelda")
    assert "Zelda" in letter
    assert constants.NAME_PLACEHOLDER not in letter


def test_read_letter_reads_file_from_folder(tmp_path: Path) -> None:
    """A template file is returned as written."""
    (tmp_path / "letter_1.txt").write_text("Hi [NAME]", encoding="utf-8")
    assert FolderLetterSource(tmp_path).read_letter(1) == "Hi [NAME]"


def test_read_letter_missing_file_raises_template_error(tmp_path: Path) -> None:
    """A missing template raises LetterTemplateError."""
    with pytest.raises(LetterTemplateError):
        FolderLetterSource(tmp_path).read_letter(1)

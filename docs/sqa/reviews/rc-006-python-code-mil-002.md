# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-006 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review of `src/` and `tests/` (MIL-002 task 6)
- Language and domain: n/a (technical type)
- Language reviewer: none (the reviewer is the stand-in for S01, who reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions and variables are snake_case, classes PascalCase, constants UPPER_SNAKE; ruff (E, F, I, B, UP) agrees. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`find_birthday_people`, `send_birthday_wishes`, `read_credentials`); no cryptic abbreviations. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass; config is in `pyproject.toml`; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict src tests` reports no issues; every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; `MailError`, `BirthdayDataError`, `LetterTemplateError` are raised `from` their cause. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default arguments (dataclass fields use `default_factory`); no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | CSV file and SMTP connection are used in `with` blocks. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a Doxygen docstring (`@brief`, `@param`, `@return`). |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `print` is used only in `presentation/cli.py` for the program output the user asked for (dry-run mail, status lines, errors to stderr); it is not diagnostic logging. The token is never printed (tested in `test_cli.py`). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists: the plan has only plain technical tasks and no use case (recorded in the Project Plan, Open Issues). The structure follows `clean-architecture`. Stand-in decision, open to challenge by S01. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 56 tests pass offline in 0.2 s; they use fakes and `tmp_path`, are named for behaviour and do not read `.env`. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Strict mode passes. `Any` appears twice for the SMTP factory type, each with a comment. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; dev extras are pytest, ruff and mypy with lower bounds. Exact pins are not set because the project has no runtime dependencies. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The placeholder, SMTP settings, subject and file names are defined once in `constants.py`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports nothing from other layers; `application` imports `domain`; `infrastructure` and `presentation` import inward. No cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change per module; ports are narrow protocols; the use case receives its collaborators. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/birthday_wisher/`; `unit`, `integration`, `e2e` under `tests/`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English, lower-case snake_case, with no spaces. |

## Overall Verdict

Go - All applicable criteria pass; criterion 10 is N-A because no Design Class Diagram exists (stand-in decision).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether a Design Class Diagram is wanted for this small project | S01 | 2026-10-20 |

---
[MIL-002]: ../../milestones/mil-002-birthday-wisher-core.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md

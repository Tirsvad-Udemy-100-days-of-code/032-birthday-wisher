# MIL-002 Birthday Wisher Core

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed in RC-004 (Go) | [052008f] |

---

## Purpose

Decide whether the birthday wisher works: it finds today's birthdays, builds a letter and sends it, with tests that need no network and no credentials.

## Deliverable

The `birthday_wisher` package: loading `birthdays.csv`, matching today's month and day, choosing a random template and replacing `[NAME]`, sending by SMTP with STARTTLS, a `main` entry point, and a pytest suite. All public items carry Doxygen comments.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes with no network access and without a `.env` file | Go | No-Go |
| 2 | A test proves that a person whose month and day equal today receives exactly one letter and nobody else does | Go | No-Go |
| 3 | A test proves that `[NAME]` is replaced and every one of the three templates can be chosen | Go | No-Go |
| 4 | A test with a fake SMTP object proves STARTTLS is called before login and that the subject is "Happy Birthday" | Go | No-Go |
| 5 | No source or test file imports or reads `.env`; the token is read from the `GMAIL_TOKEN` environment variable only | Go | No-Go |
| 6 | The code is reviewed against `qc-programming-python` and the review record says Go | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs the skeleton, constants and data files |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 3 | [BC-001] |
| S01, S02 concerns | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 - within the schedule of the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Load and match birthdays | Read `birthdays.csv` with the standard `csv` module into a dictionary keyed by `(month, day)` as the course hint describes, and return the people whose key equals today's `(month, day)`. Today is a parameter so tests can fix the date. | No |  |
| 2 | Build the letter | Choose one of the letter templates at random (the chooser is injectable for tests), and replace `[NAME]` with the person's name. Fail with a clear message when a template is missing. | No |  |
| 3 | Send the letter by SMTP | Send the letter with `smtplib`: connect to the host in `constants.py`, call `starttls()`, log in with the sender address and the `GMAIL_TOKEN` environment variable, and send with the subject "Happy Birthday". The SMTP class is injected; the token is never logged. | No |  |
| 4 | Add main entry point | Wire the pieces together in `main.py` (composition root): load, match, build, send. Add a `--dry-run` option that prints instead of sending, used for screenshots and by learners without credentials. Exit with a non-zero status on error. | No |  |
| 5 | Write pytest tests | Cover matching, letters, sending with a fake SMTP and the entry point with a fixed date. Tests use temporary files and never touch the network or `.env`. | No |  |
| 6 | Review code against the Python checklist | Review `src/` and `tests/` against `qc-programming-python`, write the `RC-*` record and fix findings before the pull request. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-001]: ./mil-001-project-setup.md
[052008f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/commit/052008f21364120a7c4d5ebbff26b8c16e05a21c

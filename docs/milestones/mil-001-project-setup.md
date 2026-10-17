# MIL-001 Project Setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed in RC-003 (Go) | [052008f] |

---

## Purpose

Decide whether the project skeleton is ready to hold code: configuration, tooling, ignore rules and repository metadata are in place and reviewed.

## Deliverable

A Python 3.13+ project skeleton: `pyproject.toml` with pytest and no runtime dependencies, `.gitignore`, `.env.example`, `src/` and `tests/` folders, `constants.py`, `Doxyfile`, `.venv` instructions, the assignment data files, and the repository description and topics on the git host. One pull request.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pip install -e .[dev]` succeeds in a fresh `.venv` and `python -m pytest` runs (a smoke test passes) | Go | No-Go |
| 2 | `pyproject.toml` requires Python `>=3.13` and lists no runtime dependencies | Go | No-Go |
| 3 | `.gitignore` ignores `.venv/`, `__pycache__/` and `.env`; `.env` is not tracked | Go | No-Go |
| 4 | `Doxyfile` exists and `doxygen Doxyfile` runs without error (or the gap is recorded) | Go | No-Go |
| 5 | Repository description and topics are set on the git host (checked through the API) | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3 (tests), objective 5 (publish) | [BC-001] |
| S01, S03 concerns | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-18 - within the schedule of the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Configure pyproject and tooling | Create `pyproject.toml` (`requires-python >=3.13`, no runtime dependencies, an optional `dev` extra with pytest, pytest configuration with `pythonpath = src`), a Python `.gitignore` that also ignores `.env`, and `.env.example` listing `GMAIL_TOKEN`. The token in `.env` is for personal use only and is never read by tests. | No |  |
| 2 | Create src and tests layout with constants.py | Create the `src/birthday_wisher/` package with `constants.py` (file names, `[NAME]` placeholder, SMTP host and port, subject, environment variable names) and a `tests/` folder with a smoke test, so later work has a place to land. | No |  |
| 3 | Add assignment data files | Add `birthdays.csv` (header `name,email,year,month,day`, dummy rows only, never a real address) and `letter_templates/letter_1.txt` to `letter_3.txt` from the course starter, keeping the `[NAME]` placeholder. | No |  |
| 4 | Add Doxyfile | Add a `Doxyfile` that documents `src/` from the Doxygen comments and writes its output to an ignored `docs/doxygen/` folder. | No |  |
| 5 | Set repository description and topics | Set the description and topics on the git host through its API, using `GITEA_TOKEN` read from the environment or `.env` without printing it. Stop and report if the token is missing or rejected. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[052008f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/commit/052008f21364120a7c4d5ebbff26b8c16e05a21c

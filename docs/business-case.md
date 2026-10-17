# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed in RC-001 (Go) | [052008f] |

---

## Executive Summary

Day 32 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" asks for an automated birthday wisher. The program reads a CSV of friends and family, checks whether today is somebody's birthday, picks one of three letter templates at random, inserts the person's name and sends the letter by e-mail through SMTP. This project builds the "normal" difficulty level as a small, readable, runnable Python 3.13+ project with tests, documentation and a tri-lingual wiki, so that course participants and repository viewers can learn from it.

## Methodological and Standards Foundation

The work follows the SQA and QC framework mounted at `framework/`: Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code, each step reviewed before the next. Quality characteristics follow ISO/IEC 25010:2023. Source code follows the `coding-conventions` skill (Python) and the `clean-architecture` skill; the code is documented with Doxygen comments.

## Problem Statement

The course assignment ships only a stub (`main.py` with hints, three letter templates and a one-row `birthdays.csv`). A learner who finishes it has working but ad-hoc code. Without a reference solution that is structured, tested and documented, other course participants cannot compare solutions, and a viewer of the repository learns little.

## Business Opportunity

A clean reference solution lets participants compare approaches, and gives GitHub viewers a small example of a tested, documented Python project with no runtime dependencies beyond the standard library.

## Objectives

1. Deliver a Python program that sends a random birthday letter, with the person's name inserted, to every person in `birthdays.csv` whose month and day match today.
2. Keep the assignment's function and file names recognisable (`birthdays.csv`, `letter_templates/letter_1.txt` to `letter_3.txt`, `[NAME]` placeholder).
3. Deliver automated tests (pytest) that run without network access or real credentials.
4. Deliver a README, a Doxygen configuration and a wiki in English, Danish and Bahasa Malaysia, with screenshots.
5. Publish the repository with a description and topics.

## Scope

### In Scope

- Reading `birthdays.csv`, matching today's month and day, choosing a random template, replacing `[NAME]`, sending by SMTP with STARTTLS (Gmail by default).
- Standard-library implementation (`csv`, `datetime`, `random`, `smtplib`); pandas is not used, to keep runtime dependencies at zero.
- `src/` and `tests/` layout, `constants.py`, `pyproject.toml`, Python `.gitignore`, `.env.example`, Doxyfile, local `.venv` instructions.
- README from the framework template and a wiki in en, da and ms, with screenshots.

### Out of Scope

- A scheduler or hosting (the program is run by hand or by the learner's own scheduler).
- A graphical user interface.
- The "hard" and "extra hard" course levels.
- Storing or testing real credentials: `.env` holds a personal token and is only for personal use; it is git-ignored, never imported by tests and never committed.

## Expected Benefits

### Tangible Benefits

- A runnable, tested reference solution with instructions.
- Tests that give a repeatable result without sending mail.

### Intangible Benefits

- Learning value for the author and for other course participants.
- A tidy example for repository viewers.

## Strategic Alignment

The project is a learning portfolio piece within the repository group Tirsvad-Udemy-100_days_of_code, and a practice run of the SQA and QC framework on a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | 100 % of pytest tests pass offline | `python -m pytest` exit code 0 |
| 2 | Runtime dependencies | 0 third-party packages | `pyproject.toml` `dependencies` is empty |
| 3 | Documentation | README plus wiki in 3 languages, each with at least one screenshot | files exist in the repository and wiki |
| 4 | Repository metadata | description and topics set | visible on the git host |
| 5 | Secrets | no secret in git history | search for the token value finds nothing |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Gmail token leaks into git or logs | High: account abuse | `.env` is git-ignored, only `.env.example` is tracked, tests never read `.env`, the token is never printed |
| Tests accidentally send mail | Medium | SMTP is injected and replaced by a fake in tests |
| Screenshots show an address or token | Medium | Screenshots use the dummy data and the dry-run output only |
| Git host token missing for topics or the wiki | Medium | Stop and report; the user supplies the token |
| Birthday on 29 February | Low | Documented behaviour: sent on 28 February in non-leap years, or a documented limitation |

## Assumptions

- The Product Owner is S01, who is also developer and reviewer; the AI authors the documents and acts as S01's stand-in in autonomous mode, recorded in each review.
- The people the project is for (S02, S03) are reached only by the user.
- The PO language is English and the domain is IT.
- Python 3.13 or newer is installed; the learner has a Gmail app password.

## Constraints

- Python 3.13 or newer, a local `.venv`, pytest for tests, constants in `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- One pull request per milestone, from a branch.
- `framework/` is not edited from this project.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| A few hours of the author's time; no licence or hosting cost | A reference solution, learning value and a portfolio entry; qualitative, as the project has no revenue |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a working, tested solution |
| S02 | Udemy coursists; want readable, runnable code with the assignment's names |
| S03 | GitHub viewers; want a clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed. The scope is small, the risk is manageable and the result has learning value.

---

[SA-001]: ./stakeholder-analysis.md
[052008f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/commit/052008f21364120a7c4d5ebbff26b8c16e05a21c

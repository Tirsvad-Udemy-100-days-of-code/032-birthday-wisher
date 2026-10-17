# MIL-003 Documentation and Publication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed in RC-005 (Go) | [052008f] |

---

## Purpose

Decide whether the project is ready for its readers: instructions, generated documentation and a tri-lingual wiki with screenshots exist and are correct.

## Deliverable

A README from the framework template with run and test instructions and screenshots; the `.venv` and `python -m pip install --upgrade pip` instructions; a wiki in `docs/wiki/` in English, Danish (`-da`) and Bahasa Malaysia (`-ms`) with the same pages and screenshots; the wiki publish workflow.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `bash framework/scripts/check-readme.sh` passes on `README.md` | Go | No-Go |
| 2 | README shows how to create and use a local `.venv`, run `python -m pip install --upgrade pip`, run the program and run the tests, and each command works as written | Go | No-Go |
| 3 | The wiki has the same page set in en, da and ms, each page with the language line, and `_Sidebar.md` lists all three | Go | No-Go |
| 4 | README and each wiki language contain at least one screenshot, and no screenshot shows an address or token | Go | No-Go |
| 5 | `bash framework/scripts/check-languages.sh` passes | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The screenshots and instructions describe the working program |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 5 | [BC-001] |
| S02 and S03 concerns | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-20 - within the schedule of the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots | Produce screenshots of a dry run, a test run and the `.venv` setup using the dummy data only, stored in `docs/images/`. Screenshots are rendered from terminal output by a script, never taken on the host desktop, and never show an address or token. | No |  |
| 2 | Write README | Create `README.md` from the framework template: overview, requirements, `.venv` and `python -m pip install --upgrade pip` setup, run, tests, license, links, appendix of project documents, and screenshots. | No |  |
| 3 | Write English wiki | Write the wiki pages in `docs/wiki/` in English (Home, Setup, Usage, Configuration, Testing, Architecture), with screenshots and a `_Sidebar.md`. | No |  |
| 4 | Translate wiki to Danish | Translate each English wiki page to `<Page>-da.md`, same page set, language line on top, code and commands unchanged. | No |  |
| 5 | Translate wiki to Bahasa Malaysia | Translate each English wiki page to `<Page>-ms.md`, same page set, language line on top, code and commands unchanged. | No |  |
| 6 | Add wiki publish workflow | Copy `framework/templates/ci/publish-wiki.yml` to the project CI folder so the wiki reaches the git host by merge. | No |  |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-002]: ./mil-002-birthday-wisher-core.md
[052008f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-birthday-wisher/commit/052008f21364120a7c4d5ebbff26b8c16e05a21c

# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed in RC-002 (Go) | pending |

---

## Purpose

This analysis names the people the project serves and what each needs, so that scope and documentation choices can be traced to a person. It classifies each stakeholder by power and interest (Mendelow grid) and maps concerns to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A working, tested solution to the assignment, built with the framework |
| S02 | Udemy coursists | Course participants who share and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews every step and accepts the result.
- **Keep Informed (S02):** cannot change the project but depends on the quality of the code and README.
- **Monitor (S03):** casual visitors; served by the repository front page.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Birthday letters are sent correctly | Functionality |
| S01 | Tests run offline and are repeatable | Reliability |
| S01 | The token never leaks | Functionality (security) |
| S02 | Assignment names (`birthdays.csv`, `[NAME]`, letter templates) are kept | Usability |
| S02 | Code is easy to read and run | Usability, Supportability |
| S03 | Description, topics and README are clear | Usability |
| S03 | No runtime dependencies | Supportability (+ implementation constraint) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Each milestone | Pull request, review record, run summary | All milestones |
| S02 | README and wiki (en, da, ms) | At publication | Run instructions with screenshots | Documentation milestone |
| S03 | Repository description, topics and README | At publication | Front page | Documentation milestone |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| The course hints use pandas, but S03 wants no runtime dependencies | S02, S03 | Use the standard `csv` module and keep the assignment's names; document the choice in the README |
| Real sending needs a secret, but the repository is public | S01, S03 | The token is read from the environment; only `.env.example` is tracked |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct sending, offline tests | [BC-001] objectives 1 and 3 |
| S02 | Assignment names, run instructions | [BC-001] objectives 2 and 4 |
| S03 | Description, topics, no dependencies | [BC-001] objectives 4 and 5 |

## Sign-Off

Reviewer: S01 (Product Owner). Review recorded in the `RC-*` for this instance.

---

[BC-001]: ./business-case.md

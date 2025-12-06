# Repository Guidelines

## Project Structure & Module Organization
- `docs/overview/`: entry-point context (e.g., `EXECUTIVE_SUMMARY.md`, `GEMINI.md`, `Instructional Prompt ULS.md`, `PROJECT_PLAN.md`).
- `docs/reviews/`: peer-review artifacts (`Peer-Review_1.md`, `Peer_Review_2.md`).
- `docs/reports/`: authored reports and analyses (`ULS_*_Report.*`, `ULS_Mobile_Game_Concepts.md`).
- `docs/whitepaper/`: source/feedback on the ULS white paper (`ULS_White_Paper_*`).
- `scripts/`: runnable code (`uls_pilot_simulation.py`, `docx_to_txt.py`); add new utilities here with concise snake_case names.
- `data/`: generated artifacts (`uls_pilot_data.csv`, `uls_pilot_statistics.json`). Keep outputs together with the simulation they stem from.

## Environment Setup & Dependencies
- Use Python 3.10+ with a local venv: `python -m venv .venv` then `.\.venv\Scripts\activate`.
- Install required libraries: `pip install numpy pandas scipy python-docx`. Keep random seeds stable for reproducibility unless you document why they changed.

## Build, Test, and Development Commands
- `python scripts\\uls_pilot_simulation.py`: Generates synthetic participant data, prints ANOVA/effect sizes, and writes `data\\uls_pilot_statistics.json` + `data\\uls_pilot_data.csv`.
- `python scripts\\docx_to_txt.py <input.docx> <output.txt>`: Converts DOCX reports to plain text for analysis or diffing.
- Run from repo root to keep relative paths stable; commit regenerated CSV/JSON alongside the code change that produced them.

## Coding Style & Naming Conventions
- Follow PEP 8: 4-space indentation, descriptive snake_case for variables/functions, and module-level constants in ALL_CAPS.
- Prefer pure functions with clear docstrings; keep I/O at the bottom of scripts under `if __name__ == "__main__"`.
- Keep notebooks/scripts deterministic: set seeds and avoid hidden global state.

## Testing Guidelines
- No formal test suite; validation is via rerunning `uls_pilot_simulation.py` and confirming key outputs (ANOVA table, effect sizes, Hybrid vs Control delta) match expectations.
- When modifying data generation, compare new summary stats to prior runs and note material shifts in commit/PR descriptions.

## Commit & Pull Request Guidelines
- Commit messages in history mix conventional commits (`feat:`, `docs:`) with short imperative summaries; prefer the conventional style and keep subjects under ~72 chars.
- PRs should include: summary of changes, files touched (especially regenerated CSV/JSON), expected numerical shifts, and any follow-up tasks.
- Avoid committing large binary exports unless essential; prefer text-based artifacts that can be diffed.

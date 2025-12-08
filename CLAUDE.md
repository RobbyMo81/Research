# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a research project repository for the **Unified Learning Stack (ULS)**, an adaptive cognitive architecture designed to optimize learning for both human and artificial intelligence systems. The repository serves as a research archive containing documentation, simulation code, and empirical data validating the ULS framework.

## Environment Setup

This repository uses Python 3.13 with a virtual environment:

```bash
# Activate virtual environment (Windows)
.\.venv\Scripts\activate

# Install dependencies
pip install numpy pandas scipy python-docx
```

**Important:** Random seeds are set to `42` in simulation scripts for reproducibility. Do not change seeds without documenting the reason in commit messages.

## Common Commands

### Running the ULS Pilot Simulation

The main simulation generates synthetic participant data (N=120) across four conditions (Control, Sung Engine, Loci Engine, Hybrid Adaptive):

```bash
# Run from repository root
python scripts\uls_pilot_simulation.py
```

This script:
- Generates `data\uls_pilot_data.csv` (participant-level data)
- Generates `data\uls_pilot_statistics.json` (ANOVA results, effect sizes, descriptive stats)
- Prints ANOVA table and Cohen's d effect sizes to console

**Validation:** After modifying simulation code, compare new outputs to previous runs and document material shifts in commit messages.

### Document Conversion Utility

```bash
# Convert DOCX to plain text
python scripts\docx_to_txt.py <input.docx> <output.txt>
```

Use this for converting `.docx` reports to text for analysis or diffing.

## Repository Structure

- **`docs/overview/`**: Entry-point documentation (`EXECUTIVE_SUMMARY.md`, `GEMINI.md`, `Instructional Prompt ULS.md`, `PROJECT_PLAN.md`)
- **`docs/reviews/`**: Peer reviews that prompted this research (`Peer-Review_1.md`, `Peer_Review_2.md`)
- **`docs/reports/`**: Research reports and analyses (`ULS_*_Report.*`, `ULS_Mobile_Game_Concepts.md`)
- **`docs/whitepaper/`**: White paper source and feedback (`ULS_White_Paper_*`)
- **`scripts/`**: Python utilities (`uls_pilot_simulation.py`, `docx_to_txt.py`)
- **`data/`**: Generated simulation outputs (CSV and JSON files)

## Key Findings

The simulation demonstrates:
- **27.6% improvement** in immediate recall for Hybrid adaptive routing vs Control (Cohen's d = 1.149, p < 0.001)
- Original white paper claim of "40-60% improvement" was **not fully supported** by simulation
- Both Sung Engine (conceptual) and Loci Engine (factual) show moderate individual effects

## Architecture Notes

### Simulation Design (`scripts/uls_pilot_simulation.py`)

The simulation is based on established effect sizes from learning science literature:

**Parameters:**
- `N_PER_CONDITION = 30` (total N=120)
- `CONDITIONS = ['Control', 'Sung', 'Loci', 'Hybrid']`
- `BASELINE_MEAN = 60.0` (control group baseline percentage)
- `SUNG_EFFECT_CONCEPTUAL = 0.7` (Cohen's d, from Dunlosky et al., 2013)
- `LOCI_EFFECT_FACTUAL = 1.0` (Cohen's d, from Bower 1970)
- `HYBRID_SYNERGY = 0.5` (hypothesized additional benefit)

**Data Structure:**
Each participant record includes:
- `participant_id`, `condition`, `ability` (latent learning ability)
- `immediate_recall`, `recall_7day`, `recall_30day` (performance metrics)
- `material_type` (Conceptual/Factual), `retention_rate_7day`, `retention_rate_30day`

**Statistical Analysis:**
- One-way ANOVA across conditions
- Pairwise t-tests with Bonferroni correction
- Cohen's d effect sizes for all comparisons

### Code Organization Principles

From `AGENTS.md`:
- Follow PEP 8 (4-space indentation, snake_case)
- Prefer pure functions with clear docstrings
- Keep I/O operations at script bottom under `if __name__ == "__main__"`
- Maintain determinism: set seeds, avoid hidden global state

## Development Workflow

1. **Run scripts from repository root** to keep relative paths stable
2. **Commit regenerated CSV/JSON files** alongside code changes that produced them
3. **Compare outputs** before and after modifications to detect material shifts
4. **Use conventional commits** (`feat:`, `docs:`, `refactor:`) with subjects under 72 characters

## Testing

No formal test suite. Validation is manual:

1. Run `python scripts\uls_pilot_simulation.py`
2. Verify outputs:
   - ANOVA table shows expected F-statistic and p-value
   - Hybrid vs Control delta is ~27.6%
   - Cohen's d effect sizes match expectations
   - CSV contains 120 rows (30 per condition)
   - JSON contains complete statistical summary

## Important Constraints

- This is a **research archive**, not production code
- Simulation is deterministic (seed=42) for reproducibility
- Generated data should be committed with the code that creates it
- Focus is on empirical validation, not software engineering best practices

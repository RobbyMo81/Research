# Unified Learning Stack (ULS) Research Project

## Project Overview

This repository houses the results of a research project focused on the **Unified Learning Stack (ULS)**, an adaptive cognitive architecture designed to optimize learning for both human and artificial intelligence systems.

The project was initiated to address critical feedback received during the peer review of the ULS White Paper (v0.4). The primary goal was to provide empirical validation (through simulation) and methodological expansion to strengthen the ULS framework.

## Key Findings from Simulation

A pilot study simulation (`uls_pilot_simulation.py`) was conducted with N=120 participants across four conditions (Control, Sung Engine, Loci Engine, Hybrid Adaptive). The key findings are:

*   **Hybrid adaptive routing shows a 27.6% improvement over the Control group** (Cohen's d = 1.149, p < 0.001) in immediate recall.
*   The ULS White Paper's original claim of a "40-60% improvement" was **not fully supported** by the simulation, which found a more modest but still significant 27.6% improvement.
*   Both the **Sung Engine** (for conceptual material) and **Loci Engine** (for factual material) showed moderate effects individually.

**Conclusion:** The dual-engine adaptive routing approach of ULS is empirically supported by this simulation, but the magnitude of benefit is more modest than initially claimed. The ULS concept holds merit but requires further human validation.

## Repository Contents

This repository is structured as a research archive, containing documentation, data, and scripts related to the ULS research project:

*   **`docs/overview/`**: Entry-point context (`EXECUTIVE_SUMMARY.md`, `GEMINI.md`, `Instructional Prompt ULS.md`, `PROJECT_PLAN.md`).
*   **`docs/reviews/`**: Peer reviews (`Peer-Review_1.md`, `Peer_Review_2.md`).
*   **`docs/reports/`**: Authored reports and analyses (`ULS_*_Report.*`, `ULS_Mobile_Game_Concepts.md`).
*   **`docs/whitepaper/`**: White paper source and feedback (`ULS_White_Paper_*`).
*   **`scripts/uls_pilot_simulation.py`**: Simulation code generating synthetic pilot data and stats.
*   **`scripts/docx_to_txt.py`**: Utility for converting `.docx` files to text.
*   **`data/uls_pilot_data.csv`** and **`data/uls_pilot_statistics.json`**: Generated data and statistics from the simulation.

## How to Navigate This Research

1.  **Start with the Executive Summary:** Begin with `docs/overview/EXECUTIVE_SUMMARY.md` for a concise overview of the project's purpose, findings, and conclusions.
2.  **Understand the Critique:** Review `docs/reviews/Peer-Review_1.md` and `docs/reviews/Peer_Review_2.md` to grasp the initial criticisms that prompted this research.
3.  **Explore the Simulation:** Examine `scripts/uls_pilot_simulation.py` to understand the data-generation methodology, then review `data/uls_pilot_data.csv` and `data/uls_pilot_statistics.json` for outputs.
4.  **Deep Dive into Reports:** Consult `docs/reports/` and `docs/whitepaper/` for detailed analyses, improvements, expansions, and validations.

This repository serves as a testament to an iterative research process, aiming to enhance scientific rigor and address the complexities of an ambitious learning framework.

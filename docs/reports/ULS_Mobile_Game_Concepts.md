# ULS Mobile Game Concepts for Mass Participation

## Evidence Review and Search Trace
- Reviewed **EXECUTIVE_SUMMARY.md** to extract core ULS elements (Sung Engine for conceptual material, Loci Engine for factual material, Hybrid adaptive routing) and current evidence strength (simulated 27.6% improvement, no human data yet). 
- Focused on documented limitations: simulated data only, narrow domain, cold-start risk, and need for human RCT validation.

## Design Principles Anchored to ULS Findings
1. **Dual-strategy practice loops**: Every play session should exercise both conceptual (Sung-style) and factual (Loci-style) encoding so we can test the Hybrid advantage noted in simulation.
2. **Adaptive routing**: Early levels randomize strategy assignments to gather baseline response; mid/late levels personalize sequencing using learner performance and spaced-retrieval curves.
3. **Instrumented experimentation**: All mechanics must log randomized A/B assignments, retention probes (immediate, 7-day, 30-day), and user context to support future human validation.
4. **Cold-start safety**: Lightweight onboarding with 3–5 quick “skill reads” before personalization to address initial uncertainty highlighted in the research.

## Game Concepts (Mass Appeal + Data Utility)
### 1) Knowledge City Run
- **Loop**: Players unlock city districts by completing micro-runs combining rhythm-based Sung prompts for concepts and AR waypoint hunts for Loci-style factual anchors.
- **Motivation**: Daily streaks, seasonal city resets, and cooperative district builds to drive retention.
- **Data hook**: Randomly assigns Sung-first vs. Loci-first routes to test ordering effects; periodic surprise quizzes on past districts support 7/30-day retention tracking.

### 2) Memory Band Battle
- **Loop**: Music-timed tap sequences teach conceptual chunks (lyrics-as-mnemonics) while stage-prop placement mini-puzzles encode factual details spatially.
- **Motivation**: Squad competitions, asynchronous duels, and unlockable songs tied to academic subjects.
- **Data hook**: Crossed factors (concept difficulty × factual density × strategy order) enable effect-size estimation of Hybrid vs. single-strategy play.

### 3) Storyforge Expedition
- **Loop**: Players co-author branching stories; plot decisions require recalling prior facts (Loci cues) and understanding concepts to progress.
- **Motivation**: User-generated arcs, social voting, and limited-time “canon events” to re-engage dormant users.
- **Data hook**: Built-in recall gates at chapter restarts measure long-delay retention; A/B of adaptive vs. fixed strategy routing.

## Live-Experiment Framework
- **Randomization tiers**: (a) Strategy order, (b) spacing interval, (c) feedback style (explicit mnemonic vs. discovery-based), (d) reward schedule.
- **Outcome metrics**: Immediate accuracy, 7/30-day retention, time-on-task, drop-off, and user-reported cognitive load.
- **Analysis plan**: Pre-register hypotheses (Hybrid > Sung-only/Loci-only by ≥10–15%), compute ANOVA/Cohen’s d mirroring the simulation, and segment by subject domain.

## Risks and Mitigations
- **Simulated evidence only** → Prioritize rapid human pilot within the app; ensure IRB/ethics and consent flows.
- **Cold start** → Short calibration sprint + default mixed-strategy path before personalization.
- **Engagement decay** → Social loops (squads, co-op builds), seasonal resets, and creator tools (maps, stories, setlists) to keep content fresh.

## Recommended Next Steps
1. Build a paper prototype of **Knowledge City Run** and run a 2-week soft launch to collect baseline Hybrid vs. single-strategy effects.
2. Instrument data pipelines for randomized assignments and retention probes before expanding content.
3. Prepare IRB-style consent and data governance for research use of in-app metrics.

---
**Conclusion:** Request further testing. The game concepts align with ULS principles and are designed to generate the human data needed to validate (or revise) the simulated 27.6% Hybrid advantage.

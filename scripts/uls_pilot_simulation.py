"""
ULS Pilot Study Data Simulation
Generates realistic pilot data based on established effect sizes from literature
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

# Directories
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# ============================================================================
# SIMULATION PARAMETERS (Based on Literature)
# ============================================================================

N_PER_CONDITION = 30
CONDITIONS = ['Control', 'Sung', 'Loci', 'Hybrid']
TOTAL_N = N_PER_CONDITION * len(CONDITIONS)

# Base performance parameters
BASELINE_MEAN = 60.0  # Control group baseline (%)
BASELINE_SD = 15.0

# Effect sizes from literature
SUNG_EFFECT_CONCEPTUAL = 0.7  # Cohen's d (Dunlosky et al., 2013)
LOCI_EFFECT_FACTUAL = 1.0     # Cohen's d (Bower, 1970; meta-analyses)
HYBRID_SYNERGY = 0.5          # Hypothesized additional benefit

# Forgetting parameters (Ebbinghaus/Wixted curves)
DECAY_7DAY = 0.20   # 20% forgetting after 7 days
DECAY_30DAY = 0.35  # 35% forgetting after 30 days

# Individual variation
INDIVIDUAL_SD = 12.0  # Between-subject variation in learning ability

# ============================================================================
# DATA GENERATION FUNCTIONS
# ============================================================================

def generate_participant_ability(n):
    """Generate underlying learning ability for each participant"""
    return np.random.normal(0, INDIVIDUAL_SD, n)

def apply_forgetting(immediate_score, days, individual_ability):
    """Apply forgetting curve based on time elapsed"""
    if days == 0:
        return immediate_score
    elif days == 7:
        decay = DECAY_7DAY
    elif days == 30:
        decay = DECAY_30DAY
    else:
        # Exponential decay for other timepoints
        decay = 1 - np.exp(-days / 30)

    # Forgetting is moderated by individual ability (better learners retain more)
    ability_modifier = 1 - (decay * (1 - individual_ability / 100))
    forgotten_score = immediate_score * ability_modifier

    # Add measurement noise
    noise = np.random.normal(0, 3)
    return np.clip(forgotten_score + noise, 0, 100)

def generate_condition_data(condition, n, item_type='mixed'):
    """
    Generate data for a specific condition

    Args:
        condition: 'Control', 'Sung', 'Loci', or 'Hybrid'
        n: number of participants
        item_type: 'conceptual', 'factual', or 'mixed'
    """
    # Generate individual learning ability
    ability = generate_participant_ability(n)

    # Base score (control condition)
    base_score = BASELINE_MEAN + ability

    # Apply condition-specific effects
    if condition == 'Control':
        immediate_score = base_score + np.random.normal(0, BASELINE_SD, n)

    elif condition == 'Sung':
        if item_type == 'conceptual':
            # Large effect on conceptual items
            boost = SUNG_EFFECT_CONCEPTUAL * BASELINE_SD
            immediate_score = base_score + boost + np.random.normal(0, BASELINE_SD, n)
        elif item_type == 'factual':
            # Small/no effect on factual items (not designed for this)
            boost = 0.2 * BASELINE_SD  # Minimal benefit
            immediate_score = base_score + boost + np.random.normal(0, BASELINE_SD, n)
        else:  # mixed
            # Average of conceptual and factual effects
            boost = (SUNG_EFFECT_CONCEPTUAL * 0.5 + 0.2 * 0.5) * BASELINE_SD
            immediate_score = base_score + boost + np.random.normal(0, BASELINE_SD, n)

    elif condition == 'Loci':
        if item_type == 'factual':
            # Large effect on factual items
            boost = LOCI_EFFECT_FACTUAL * BASELINE_SD
            immediate_score = base_score + boost + np.random.normal(0, BASELINE_SD, n)
        elif item_type == 'conceptual':
            # Poor performance on conceptual items (not designed for this)
            boost = 0.3 * BASELINE_SD  # Minimal benefit
            immediate_score = base_score + boost + np.random.normal(0, BASELINE_SD, n)
        else:  # mixed
            # Average of factual and conceptual effects
            boost = (LOCI_EFFECT_FACTUAL * 0.5 + 0.3 * 0.5) * BASELINE_SD
            immediate_score = base_score + boost + np.random.normal(0, BASELINE_SD, n)

    elif condition == 'Hybrid':
        if item_type == 'conceptual':
            # Sung method effect (routed correctly)
            boost = SUNG_EFFECT_CONCEPTUAL * BASELINE_SD
        elif item_type == 'factual':
            # Loci method effect (routed correctly)
            boost = LOCI_EFFECT_FACTUAL * BASELINE_SD
        else:  # mixed
            # Optimal routing + synergy effect
            avg_boost = (SUNG_EFFECT_CONCEPTUAL + LOCI_EFFECT_FACTUAL) / 2 * BASELINE_SD
            synergy_boost = HYBRID_SYNERGY * BASELINE_SD
            boost = avg_boost + synergy_boost

        immediate_score = base_score + boost + np.random.normal(0, BASELINE_SD, n)

    # Clip to valid range
    immediate_score = np.clip(immediate_score, 0, 100)

    return immediate_score, ability

def generate_full_dataset():
    """Generate complete pilot study dataset"""
    data = []
    participant_id = 1

    for condition in CONDITIONS:
        n = N_PER_CONDITION

        # Generate scores for conceptual items
        conceptual_immediate, ability = generate_condition_data(condition, n, 'conceptual')
        conceptual_7day = np.array([apply_forgetting(score, 7, ab)
                                     for score, ab in zip(conceptual_immediate, ability)])
        conceptual_30day = np.array([apply_forgetting(score, 30, ab)
                                      for score, ab in zip(conceptual_immediate, ability)])

        # Generate scores for factual items
        factual_immediate, _ = generate_condition_data(condition, n, 'factual')
        factual_7day = np.array([apply_forgetting(score, 7, ab)
                                  for score, ab in zip(factual_immediate, ability)])
        factual_30day = np.array([apply_forgetting(score, 30, ab)
                                   for score, ab in zip(factual_immediate, ability)])

        # Total scores (average of conceptual and factual)
        total_immediate = (conceptual_immediate + factual_immediate) / 2
        total_7day = (conceptual_7day + factual_7day) / 2
        total_30day = (conceptual_30day + factual_30day) / 2

        # Create participant records
        for i in range(n):
            data.append({
                'participant_id': participant_id,
                'condition': condition,
                'ability': ability[i],

                # Conceptual scores
                'conceptual_immediate': conceptual_immediate[i],
                'conceptual_7day': conceptual_7day[i],
                'conceptual_30day': conceptual_30day[i],

                # Factual scores
                'factual_immediate': factual_immediate[i],
                'factual_7day': factual_7day[i],
                'factual_30day': factual_30day[i],

                # Total scores
                'total_immediate': total_immediate[i],
                'total_7day': total_7day[i],
                'total_30day': total_30day[i],
            })
            participant_id += 1

    return pd.DataFrame(data)

# ============================================================================
# STATISTICAL ANALYSIS FUNCTIONS
# ============================================================================

def cohens_d(group1, group2):
    """Calculate Cohen's d effect size"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std

def calculate_effect_sizes(df, outcome='total_immediate'):
    """Calculate all pairwise effect sizes"""
    results = []
    conditions = df['condition'].unique()

    for i, cond1 in enumerate(conditions):
        for cond2 in conditions[i+1:]:
            group1 = df[df['condition'] == cond1][outcome].values
            group2 = df[df['condition'] == cond2][outcome].values

            d = cohens_d(group1, group2)
            t_stat, p_value = stats.ttest_ind(group1, group2)

            results.append({
                'comparison': f'{cond1} vs {cond2}',
                'cohens_d': d,
                't_statistic': t_stat,
                'p_value': p_value,
                'mean_diff': np.mean(group1) - np.mean(group2),
                'outcome': outcome
            })

    return pd.DataFrame(results)

def run_anova(df, outcome='total_immediate'):
    """Run one-way ANOVA"""
    groups = [df[df['condition'] == cond][outcome].values
              for cond in CONDITIONS]
    f_stat, p_value = stats.f_oneway(*groups)
    return {'F': f_stat, 'p': p_value, 'outcome': outcome}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == '__main__':
    print("Generating ULS Pilot Study Data...")
    print(f"Total N = {TOTAL_N} ({N_PER_CONDITION} per condition)")
    print(f"Conditions: {CONDITIONS}")
    print()

    # Generate dataset
    df = generate_full_dataset()

    # Save raw data
    data_csv = DATA_DIR / 'uls_pilot_data.csv'
    df.to_csv(data_csv, index=False)
    print(f"[OK] Raw data saved to: {data_csv.relative_to(ROOT_DIR)}")

    # Generate descriptive statistics
    print("\n" + "="*70)
    print("DESCRIPTIVE STATISTICS - Immediate Recall (Total Score)")
    print("="*70)
    desc = df.groupby('condition')['total_immediate'].describe()
    print(desc)

    # Run ANOVA
    print("\n" + "="*70)
    print("ONE-WAY ANOVA - Immediate Recall")
    print("="*70)
    anova_result = run_anova(df, 'total_immediate')
    print(f"F({len(CONDITIONS)-1}, {TOTAL_N-len(CONDITIONS)}) = {anova_result['F']:.3f}")
    print(f"p-value = {anova_result['p']:.6f}")

    # Calculate effect sizes
    print("\n" + "="*70)
    print("PAIRWISE EFFECT SIZES (Cohen's d) - Immediate Recall")
    print("="*70)
    effect_sizes = calculate_effect_sizes(df, 'total_immediate')
    print(effect_sizes.to_string(index=False))

    # Key comparison: Hybrid vs Control
    print("\n" + "="*70)
    print("KEY FINDING: Hybrid vs Control")
    print("="*70)
    hybrid_vs_control = effect_sizes[effect_sizes['comparison'] == 'Control vs Hybrid']
    if not hybrid_vs_control.empty:
        row = hybrid_vs_control.iloc[0]
        print(f"Cohen's d = {abs(row['cohens_d']):.3f}")
        print(f"Mean difference = {abs(row['mean_diff']):.2f} percentage points")
        print(f"p-value = {row['p_value']:.6f}")

        # Calculate percentage improvement
        control_mean = df[df['condition'] == 'Control']['total_immediate'].mean()
        hybrid_mean = df[df['condition'] == 'Hybrid']['total_immediate'].mean()
        pct_improvement = ((hybrid_mean - control_mean) / control_mean) * 100
        print(f"Percentage improvement = {pct_improvement:.1f}%")

        # Compare to ULS claim (40-60%)
        print(f"\nULS White Paper Claim: 40-60% improvement")
        if 40 <= pct_improvement <= 60:
            print("[OK] Claim SUPPORTED by simulation")
        else:
            print(f"[FAIL] Claim NOT supported (found {pct_improvement:.1f}%)")

    # Save all statistics to JSON
    stats_output = {
        'descriptive_stats': desc.to_dict(),
        'anova': anova_result,
        'effect_sizes': effect_sizes.to_dict('records')
    }

    stats_json = DATA_DIR / 'uls_pilot_statistics.json'
    with open(stats_json, 'w') as f:
        json.dump(stats_output, f, indent=2)

    print(f"\n[OK] Statistics saved to: {stats_json.relative_to(ROOT_DIR)}")
    print("\nData generation complete!")

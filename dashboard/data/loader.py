"""
Sentinel Health pilot data loader.

Loads sentinel_health_pilot.csv if present; otherwise synthetic fallback so
the dashboard always runs. Computes the brief's prescribed derived columns.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


DATA_DIR = Path(__file__).resolve().parent
ER_COST_USD = 1_400        # rough US-average ER visit cost (assumption — flag in UI)
HOSP_COST_USD = 13_000     # rough US-average inpatient admission cost


# Direction of improvement per clinical metric (from Elise's brief).
# True  = lower is better;  False = higher is better.
LOWER_IS_BETTER: dict[str, bool] = {
    "baseline_a1c": True,
    "baseline_systolic_bp": True,
    "baseline_weight_kg": True,
    "baseline_spo2": False,
}


@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
    csv_path = DATA_DIR / "sentinel_health_pilot.csv"
    if csv_path.exists():
        df = pd.read_csv(csv_path, parse_dates=["enrollment_date"])
    else:
        df = _fallback()
    return _enrich(df)


def _enrich(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Outcome deltas (positive = improvement, i.e. fewer events)
    df["er_reduction"] = df["er_visits_12mo_pre"] - df["er_visits_during_program"]
    df["hosp_reduction"] = df["hospitalizations_12mo_pre"] - df["hospitalizations_during_program"]

    # Call completion rate
    df["call_completion_rate"] = np.where(
        df["care_calls_scheduled"] > 0,
        df["care_calls_completed"] / df["care_calls_scheduled"],
        np.nan,
    )

    # Age bands
    df["age_band"] = pd.cut(
        df["age"],
        bins=[0, 55, 70, 200],
        labels=["<55", "55–69", "70+"],
        include_lowest=True,
    )

    # Engagement tier (quartile of weekly readings)
    df["engagement_tier"] = pd.qcut(
        df["avg_weekly_readings"],
        q=4,
        labels=["Q1 (lowest)", "Q2", "Q3", "Q4 (highest)"],
        duplicates="drop",
    )

    # Risk tier
    df["risk_tier"] = pd.cut(
        df["baseline_risk_score"],
        bins=[0, 3.5, 6.5, 10.01],
        labels=["Low", "Medium", "High"],
        include_lowest=True,
    )

    # Clinical-metric improvement %, sign-corrected to "% improvement"
    pct: list[float] = []
    for name, baseline, latest in zip(df["baseline_metric_name"], df["baseline_metric_value"], df["latest_metric_value"]):
        if pd.isna(baseline) or baseline == 0 or pd.isna(latest):
            pct.append(np.nan)
            continue
        raw = (latest - baseline) / baseline * 100.0
        lower_better = LOWER_IS_BETTER.get(name, True)
        pct.append(-raw if lower_better else raw)
    df["clinical_improvement_pct"] = pct

    # Cost-benefit
    df["estimated_savings_usd"] = df["er_reduction"] * ER_COST_USD + df["hosp_reduction"] * HOSP_COST_USD
    df["net_value_usd"] = df["estimated_savings_usd"] - df["total_cost_to_date_usd"]

    return df


def _fallback(n: int = 250, seed: int = 7) -> pd.DataFrame:
    """Last-resort synthetic data shaped like the Sentinel pilot CSV."""
    rng = np.random.default_rng(seed)
    sites = ["Hilltop Primary Care", "Westgate Clinic", "Lakeshore Health",
             "Riverside Family Med", "Cedar Park Clinic", "North Bay Internal Med"]
    conditions = ["Type 2 Diabetes", "Hypertension", "CHF", "COPD"]
    devices = ["BP Monitor", "Glucometer", "Multi-device", "Pulse Oximeter"]
    enroll_starts = pd.to_datetime("2025-08-01") + pd.to_timedelta(rng.integers(0, 280, n), unit="D")
    return pd.DataFrame({
        "patient_id": [f"P{i:04d}" for i in range(1, n + 1)],
        "enrollment_date": enroll_starts,
        "days_enrolled": (pd.Timestamp("2026-05-18") - enroll_starts).dt.days,
        "clinic_site": rng.choice(sites, n),
        "age": rng.integers(28, 93, n),
        "gender": rng.choice(["Female", "Male", "Non-binary"], n, p=[0.52, 0.46, 0.02]),
        "primary_condition": rng.choice(conditions, n),
        "baseline_risk_score": np.clip(rng.normal(5, 2, n), 1, 10).round(1),
        "device_type": rng.choice(devices, n),
        "avg_weekly_readings": np.clip(rng.normal(5, 2.5, n), 0, 14).round(1),
        "app_logins_per_month": rng.integers(0, 30, n),
        "care_calls_scheduled": rng.integers(8, 36, n),
        "care_calls_completed": rng.integers(0, 35, n),
        "alerts_triggered": rng.integers(0, 25, n),
        "baseline_metric_name": rng.choice(list(LOWER_IS_BETTER.keys()), n),
        "baseline_metric_value": rng.normal(120, 30, n).round(1),
        "latest_metric_value": rng.normal(115, 30, n).round(1),
        "er_visits_12mo_pre": rng.integers(0, 6, n),
        "er_visits_during_program": rng.integers(0, 5, n),
        "hospitalizations_12mo_pre": rng.integers(0, 4, n),
        "hospitalizations_during_program": rng.integers(0, 3, n),
        "medication_adherence_pct": rng.integers(50, 100, n),
        "patient_satisfaction_5pt": np.clip(rng.normal(4.0, 0.7, n), 1, 5).round(1),
        "monthly_program_cost_usd": np.clip(rng.normal(150, 12, n), 100, 200).round(2),
        "total_cost_to_date_usd": np.clip(rng.normal(900, 300, n), 100, 2000).round(2),
        "status": rng.choice(["Active", "Disengaged", "Withdrew", "Completed"], n, p=[0.78, 0.10, 0.05, 0.07]),
    })


def dataset_info(df: pd.DataFrame) -> dict:
    csv_path = DATA_DIR / "sentinel_health_pilot.csv"
    return {
        "source": csv_path.name if csv_path.exists() else "synthetic fallback",
        "is_real": csv_path.exists(),
        "rows": len(df),
        "cols": len(df.columns),
        "sites": int(df["clinic_site"].nunique()),
        "conditions": int(df["primary_condition"].nunique()),
        "description": (
            "Sentinel Health RPM pilot — 250 patients across 6 clinics, 9 months in. "
            "Synthetic data from Elise; safe to display. Scenario: MeridianCare Health Network, "
            "Board decision in 4 weeks on system-wide scale-up vs. sunset."
        ),
    }

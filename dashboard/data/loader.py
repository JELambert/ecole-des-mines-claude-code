"""
Dataset loader. Prefers a real file in dashboard/data/ if present; otherwise
generates a deterministic synthetic dataset so the dashboard always runs.

Supported real-data formats (auto-detected): .csv, .xlsx, .parquet
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


DATA_DIR = Path(__file__).resolve().parent


@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
    """Load the first real dataset found in the data dir, else synthetic."""
    for path in sorted(DATA_DIR.iterdir()):
        if path.is_file() and path.suffix.lower() in {".csv", ".xlsx", ".parquet"}:
            return _load_real(path)
    return _synthetic()


def _load_real(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() == ".xlsx":
        return pd.read_excel(path)
    if path.suffix.lower() == ".parquet":
        return pd.read_parquet(path)
    raise ValueError(f"Unsupported file: {path}")


def _synthetic(n_rows: int = 1500, seed: int = 42) -> pd.DataFrame:
    """Plausible health-informatics-shaped synthetic data.

    Domain is digital health (Elise's field) so the demo's framing transfers
    when real data arrives.
    """
    rng = np.random.default_rng(seed)
    start = dt.date(2025, 1, 1)
    dates = [start + dt.timedelta(days=int(d)) for d in rng.integers(0, 500, n_rows)]
    categories = rng.choice(
        ["primary_care", "specialty", "telehealth", "emergency"],
        size=n_rows,
        p=[0.45, 0.25, 0.20, 0.10],
    )
    regions = rng.choice(["North", "South", "East", "West"], size=n_rows)
    age_groups = rng.choice(["18-34", "35-54", "55-74", "75+"], size=n_rows, p=[0.25, 0.35, 0.25, 0.15])
    visit_minutes = np.clip(rng.normal(22, 9, n_rows), 3, 90).round(1)
    satisfaction = np.clip(rng.normal(4.1, 0.6, n_rows), 1, 5).round(2)
    cost_eur = np.clip(rng.normal(85, 35, n_rows), 5, 400).round(2)
    return pd.DataFrame(
        {
            "date": pd.to_datetime(dates),
            "category": categories,
            "region": regions,
            "age_group": age_groups,
            "visit_minutes": visit_minutes,
            "satisfaction": satisfaction,
            "cost_eur": cost_eur,
        }
    ).sort_values("date").reset_index(drop=True)


def dataset_info(df: pd.DataFrame) -> dict:
    real_files = [p for p in DATA_DIR.iterdir() if p.is_file() and p.suffix.lower() in {".csv", ".xlsx", ".parquet"}]
    if real_files:
        return {
            "source": real_files[0].name,
            "description": "Real dataset provided for the lecture.",
            "rows": len(df),
            "cols": len(df.columns),
        }
    return {
        "source": "synthetic (digital-health-shaped)",
        "description": "Synthetic placeholder so the dashboard runs without the real data. Drop a CSV/XLSX/Parquet into dashboard/data/ and reload.",
        "rows": len(df),
        "cols": len(df.columns),
    }

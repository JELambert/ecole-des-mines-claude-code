"""Sidebar filters tuned to the Sentinel Health schema."""

from __future__ import annotations

import pandas as pd
import streamlit as st


def render_sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")
    out = df.copy()

    for col, label in [
        ("clinic_site", "Clinic site"),
        ("primary_condition", "Primary condition"),
        ("status", "Patient status"),
        ("age_band", "Age band"),
        ("risk_tier", "Baseline risk"),
    ]:
        if col not in out.columns:
            continue
        options = sorted(out[col].dropna().astype(str).unique().tolist())
        picked = st.sidebar.multiselect(label, options, default=options)
        if picked:
            out = out[out[col].astype(str).isin(picked)]

    st.sidebar.caption(f"{len(out):,} of {len(df):,} patients after filters")
    st.sidebar.divider()
    st.sidebar.caption(
        "Cost assumptions:\n"
        "- ER visit ≈ **$1,400**\n"
        "- Hospitalization ≈ **$13,000**\n\n"
        "Rough US averages. Tune for your market."
    )
    return out

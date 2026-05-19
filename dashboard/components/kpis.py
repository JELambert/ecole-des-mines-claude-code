"""KPI strip — picks sensible default metrics from whatever numeric columns exist."""

from __future__ import annotations

import pandas as pd
import streamlit as st


def render_kpi_row(df: pd.DataFrame) -> None:
    numeric = df.select_dtypes(include=["number"]).columns.tolist()
    cols = st.columns(min(4, max(1, 1 + len(numeric[:3]))))

    cols[0].metric("Rows", f"{len(df):,}")
    for i, col in enumerate(numeric[:3], start=1):
        value = df[col].mean()
        cols[i].metric(f"avg {col}", f"{value:,.2f}" if pd.notna(value) else "—")

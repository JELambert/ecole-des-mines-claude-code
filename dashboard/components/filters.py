"""Sidebar filters that adapt to whichever columns the dataset actually has."""

from __future__ import annotations

import pandas as pd
import streamlit as st


def render_sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")
    out = df.copy()

    # Date range filter — only if a date column exists
    date_col = _first_datetime_col(out)
    if date_col:
        min_d, max_d = out[date_col].min(), out[date_col].max()
        rng = st.sidebar.date_input(
            f"{date_col} range",
            value=(min_d.date(), max_d.date()),
            min_value=min_d.date(),
            max_value=max_d.date(),
        )
        if isinstance(rng, tuple) and len(rng) == 2:
            lo, hi = pd.Timestamp(rng[0]), pd.Timestamp(rng[1]) + pd.Timedelta(days=1)
            out = out[(out[date_col] >= lo) & (out[date_col] < hi)]

    # Categorical filters — for any low-cardinality string column
    for col in out.select_dtypes(include=["object", "category"]).columns:
        uniques = sorted(out[col].dropna().unique().tolist())
        if 2 <= len(uniques) <= 20:
            picked = st.sidebar.multiselect(col, uniques, default=uniques)
            if picked:
                out = out[out[col].isin(picked)]

    st.sidebar.caption(f"{len(out):,} of {len(df):,} rows after filters")
    return out


def _first_datetime_col(df: pd.DataFrame) -> str | None:
    for c in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            return c
    return None

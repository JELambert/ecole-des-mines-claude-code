"""Charts — graceful when columns are missing."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st


def render_trend_chart(df: pd.DataFrame) -> None:
    date_col = _first_datetime_col(df)
    numeric = df.select_dtypes(include=["number"]).columns.tolist()
    if not date_col or not numeric:
        st.info("Need a date column and at least one numeric column for a trend.")
        return
    metric = st.selectbox("Metric", numeric, key="trend_metric")
    grouped = df.groupby(pd.Grouper(key=date_col, freq="W"))[metric].mean().reset_index()
    fig = px.line(grouped, x=date_col, y=metric, markers=True)
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=350)
    st.plotly_chart(fig, use_container_width=True)


def render_breakdown_chart(df: pd.DataFrame) -> None:
    cats = [c for c in df.select_dtypes(include=["object", "category"]).columns if 2 <= df[c].nunique() <= 20]
    numeric = df.select_dtypes(include=["number"]).columns.tolist()
    if not cats or not numeric:
        st.info("Need a categorical column and a numeric column for a breakdown.")
        return
    by = st.selectbox("By", cats, key="breakdown_by")
    metric = st.selectbox("Metric", numeric, key="breakdown_metric")
    agg = df.groupby(by)[metric].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(agg, x=by, y=metric)
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=350)
    st.plotly_chart(fig, use_container_width=True)


def _first_datetime_col(df: pd.DataFrame) -> str | None:
    for c in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            return c
    return None

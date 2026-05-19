"""
École des Mines guest lecture — live demo dashboard.

Runs out of the box on synthetic data so the lecture is never blocked on
Elise's dataset arriving. When a real file lands in dashboard/data/, the
loader auto-prefers it.

Run:
    uv run streamlit run app.py
"""

from __future__ import annotations

import streamlit as st

from components.kpis import render_kpi_row
from components.charts import render_trend_chart, render_breakdown_chart
from components.filters import render_sidebar_filters
from data.loader import load_dataset, dataset_info


st.set_page_config(
    page_title="École des Mines — Claude Code Demo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---- Header --------------------------------------------------------------

st.title("Built-with-Claude-Code Dashboard")
st.caption("École des Mines · 2026-05-22 · guest lecture by Joshua E. Lambert")


# ---- Data ----------------------------------------------------------------

df_raw = load_dataset()
info = dataset_info(df_raw)

with st.expander(f"Dataset: {info['source']}  ·  {info['rows']:,} rows × {info['cols']} columns", expanded=False):
    st.write(info["description"])
    st.dataframe(df_raw.head(20), use_container_width=True)


# ---- Filters -------------------------------------------------------------

df = render_sidebar_filters(df_raw)


# ---- KPI row -------------------------------------------------------------

render_kpi_row(df)


# ---- Charts --------------------------------------------------------------

left, right = st.columns(2)
with left:
    st.subheader("Trend")
    render_trend_chart(df)
with right:
    st.subheader("Breakdown")
    render_breakdown_chart(df)


# ---- Drill-down table ----------------------------------------------------

st.subheader("Detail")
st.dataframe(df, use_container_width=True, height=380)


# ---- Footer --------------------------------------------------------------

st.divider()
st.caption(
    "Source code: github.com/JELambert/ecole-des-mines-2026  ·  "
    "Built with Claude Code in <2 hours of wall time."
)

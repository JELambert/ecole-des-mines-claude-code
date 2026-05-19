"""
Sentinel Health pilot dashboard — Maya Chen's board-prep tool.

Built live (via Claude Code) for the 2026-05-22 École des Mines guest
session. Audience: Texas healthcare administrators.
"""

from __future__ import annotations

import streamlit as st

from components.charts import (
    render_cost_benefit,
    render_engagement_scatter,
    render_outcomes_panel,
    render_segment_cuts,
    render_site_performance,
)
from components.filters import render_sidebar_filters
from components.kpis import render_kpi_row
from data.loader import dataset_info, load_dataset


st.set_page_config(
    page_title="Sentinel Health — Board Prep",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---- Header --------------------------------------------------------------

st.title("Sentinel Health — Remote Patient Monitoring Pilot")
st.caption(
    "MeridianCare Health Network · 9-month snapshot · Board decision in 4 weeks: "
    "scale system-wide (~12,000 patients) or sunset."
)


# ---- Data ----------------------------------------------------------------

df_raw = load_dataset()
info = dataset_info(df_raw)

with st.expander(
    f"Dataset: **{info['source']}** · {info['rows']:,} patients × {info['cols']} columns · "
    f"{info['sites']} sites · {info['conditions']} conditions",
    expanded=False,
):
    st.markdown(info["description"])
    st.dataframe(df_raw.head(20), use_container_width=True)


# ---- Filters -------------------------------------------------------------

df = render_sidebar_filters(df_raw)


# ---- 1. KPI strip --------------------------------------------------------

st.subheader("The six numbers Maya checks first")
render_kpi_row(df)


# ---- 2. Outcomes (Question 1) -------------------------------------------

st.subheader("Question 1 — Are we reducing ER visits and hospitalizations?")
render_outcomes_panel(df)


# ---- 3. Site performance (Question 4) ----------------------------------

st.subheader("Question 4 — Which sites are succeeding, which are struggling?")
render_site_performance(df)


# ---- 4. Engagement vs outcomes (Question 3) ----------------------------

st.subheader("Question 3 — Does engagement correlate with outcomes?")
render_engagement_scatter(df)


# ---- 5. Segment cuts (Question 2) --------------------------------------

st.subheader("Question 2 — Which segments benefit most?")
render_segment_cuts(df)


# ---- 6. Cost-benefit (Question 5) --------------------------------------

st.subheader("Question 5 — Does the $1,800/patient/year cost pay for itself?")
render_cost_benefit(df)


# ---- Detail table -------------------------------------------------------

with st.expander("Patient-level detail", expanded=False):
    st.dataframe(df, use_container_width=True, height=420)


# ---- Footer -------------------------------------------------------------

st.divider()
st.caption(
    "Source code: github.com/JELambert/ecole-des-mines-2026  ·  "
    "Built with Claude Code as the worked example for the École des Mines guest session."
)

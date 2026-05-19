"""KPI strip — the six numbers Maya looks at first."""

from __future__ import annotations

import pandas as pd
import streamlit as st


def render_kpi_row(df: pd.DataFrame) -> None:
    n = len(df)
    if n == 0:
        st.info("No patients match the current filters.")
        return

    active_rate = (df["status"] == "Active").mean() * 100
    er_pre = df["er_visits_12mo_pre"].sum()
    er_dur = df["er_visits_during_program"].sum()
    er_reduction_pct = (1 - er_dur / er_pre) * 100 if er_pre else 0
    hosp_pre = df["hospitalizations_12mo_pre"].sum()
    hosp_dur = df["hospitalizations_during_program"].sum()
    hosp_reduction_pct = (1 - hosp_dur / hosp_pre) * 100 if hosp_pre else 0
    avg_sat = df["patient_satisfaction_5pt"].mean()
    total_cost = df["total_cost_to_date_usd"].sum()

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Enrolled", f"{n:,}")
    c2.metric("Active", f"{active_rate:.0f}%")
    c3.metric("ER reduction", f"{er_reduction_pct:.0f}%", delta=f"{er_pre - er_dur:+d} visits")
    c4.metric("Hospitalization reduction", f"{hosp_reduction_pct:.0f}%", delta=f"{hosp_pre - hosp_dur:+d} admits")
    c5.metric("Avg satisfaction", f"{avg_sat:.2f} / 5")
    c6.metric("Program cost to date", f"${total_cost:,.0f}")

"""Charts for the Sentinel Health dashboard. One function per panel — each
is small so live-demo extensions are clean diffs Claude Code can show."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st


# ---- Outcomes (pre vs during) -------------------------------------------

def render_outcomes_panel(df: pd.DataFrame) -> None:
    if df.empty:
        return
    summary = (
        df.groupby("primary_condition")[
            ["er_visits_12mo_pre", "er_visits_during_program",
             "hospitalizations_12mo_pre", "hospitalizations_during_program"]
        ].sum().reset_index()
    )

    er = summary.melt(
        id_vars="primary_condition",
        value_vars=["er_visits_12mo_pre", "er_visits_during_program"],
        var_name="period", value_name="er_visits",
    )
    er["period"] = er["period"].map({"er_visits_12mo_pre": "Pre-enrollment", "er_visits_during_program": "During program"})
    fig_er = px.bar(er, x="primary_condition", y="er_visits", color="period",
                    barmode="group", title="ER visits — pre vs during, by condition")
    fig_er.update_layout(margin=dict(l=10, r=10, t=40, b=10), height=340, legend_title_text="")

    hosp = summary.melt(
        id_vars="primary_condition",
        value_vars=["hospitalizations_12mo_pre", "hospitalizations_during_program"],
        var_name="period", value_name="hospitalizations",
    )
    hosp["period"] = hosp["period"].map({"hospitalizations_12mo_pre": "Pre-enrollment", "hospitalizations_during_program": "During program"})
    fig_h = px.bar(hosp, x="primary_condition", y="hospitalizations", color="period",
                   barmode="group", title="Hospitalizations — pre vs during, by condition",
                   color_discrete_sequence=px.colors.qualitative.Set2)
    fig_h.update_layout(margin=dict(l=10, r=10, t=40, b=10), height=340, legend_title_text="")

    left, right = st.columns(2)
    left.plotly_chart(fig_er, use_container_width=True)
    right.plotly_chart(fig_h, use_container_width=True)


# ---- Site performance ---------------------------------------------------

def render_site_performance(df: pd.DataFrame) -> None:
    if df.empty:
        return
    g = df.groupby("clinic_site").agg(
        patients=("patient_id", "count"),
        avg_weekly_readings=("avg_weekly_readings", "mean"),
        call_completion=("call_completion_rate", "mean"),
        er_reduction_pct=("er_visits_12mo_pre", lambda s: (
            (df.loc[s.index, "er_visits_12mo_pre"].sum() - df.loc[s.index, "er_visits_during_program"].sum())
            / max(df.loc[s.index, "er_visits_12mo_pre"].sum(), 1) * 100
        )),
        hosp_reduction_pct=("hospitalizations_12mo_pre", lambda s: (
            (df.loc[s.index, "hospitalizations_12mo_pre"].sum() - df.loc[s.index, "hospitalizations_during_program"].sum())
            / max(df.loc[s.index, "hospitalizations_12mo_pre"].sum(), 1) * 100
        )),
        net_value=("net_value_usd", "sum"),
    ).round(1).sort_values("er_reduction_pct", ascending=False)

    st.markdown("**Site performance** — sorted by ER reduction %")
    st.dataframe(
        g.style.background_gradient(subset=["er_reduction_pct", "hosp_reduction_pct"], cmap="RdYlGn")
              .background_gradient(subset=["net_value"], cmap="RdYlGn")
              .format({
                  "avg_weekly_readings": "{:.1f}",
                  "call_completion": "{:.0%}",
                  "er_reduction_pct": "{:+.0f}%",
                  "hosp_reduction_pct": "{:+.0f}%",
                  "net_value": "${:,.0f}",
              }),
        use_container_width=True,
        height=260,
    )


# ---- Engagement vs outcomes --------------------------------------------

def render_engagement_scatter(df: pd.DataFrame) -> None:
    if df.empty:
        return
    plot = df.copy()
    plot["risk_tier_str"] = plot["risk_tier"].astype(str)
    fig = px.scatter(
        plot, x="avg_weekly_readings", y="er_reduction",
        size="baseline_risk_score", color="primary_condition",
        hover_data=["patient_id", "clinic_site", "age", "status", "net_value_usd"],
        title="Engagement vs. ER reduction (size = baseline risk)",
    )
    fig.update_layout(margin=dict(l=10, r=10, t=40, b=10), height=380, legend_title_text="")
    st.plotly_chart(fig, use_container_width=True)


# ---- Segment cuts -------------------------------------------------------

def render_segment_cuts(df: pd.DataFrame) -> None:
    if df.empty:
        return
    left, right = st.columns(2)

    by_age = df.groupby("age_band", observed=True).agg(
        er_pre=("er_visits_12mo_pre", "sum"),
        er_dur=("er_visits_during_program", "sum"),
    )
    by_age["er_reduction_pct"] = (1 - by_age["er_dur"] / by_age["er_pre"].replace(0, pd.NA)) * 100
    fig_age = px.bar(by_age.reset_index(), x="age_band", y="er_reduction_pct",
                     title="ER reduction % by age band")
    fig_age.update_layout(margin=dict(l=10, r=10, t=40, b=10), height=320)
    left.plotly_chart(fig_age, use_container_width=True)

    by_risk = df.groupby("risk_tier", observed=True).agg(
        er_pre=("er_visits_12mo_pre", "sum"),
        er_dur=("er_visits_during_program", "sum"),
    )
    by_risk["er_reduction_pct"] = (1 - by_risk["er_dur"] / by_risk["er_pre"].replace(0, pd.NA)) * 100
    fig_risk = px.bar(by_risk.reset_index(), x="risk_tier", y="er_reduction_pct",
                      title="ER reduction % by baseline risk tier",
                      color_discrete_sequence=["#7c3aed"])
    fig_risk.update_layout(margin=dict(l=10, r=10, t=40, b=10), height=320)
    right.plotly_chart(fig_risk, use_container_width=True)


# ---- Cost-benefit -------------------------------------------------------

def render_cost_benefit(df: pd.DataFrame) -> None:
    if df.empty:
        return
    savings = df["estimated_savings_usd"].sum()
    cost = df["total_cost_to_date_usd"].sum()
    net = savings - cost
    roi = (net / cost) if cost else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Estimated avoided cost", f"${savings:,.0f}",
              help="ER reduction × $1,400 + Hospitalization reduction × $13,000")
    c2.metric("Program cost to date", f"${cost:,.0f}")
    c3.metric("Net value", f"${net:,.0f}")
    c4.metric("ROI", f"{roi:+.1%}")

    st.caption(
        "⚠️ Assumes US-average per-event costs ($1,400/ER, $13,000/hospitalization). "
        "Replace with MeridianCare's contracted rates for board-grade numbers."
    )

# Sentinel Health RPM Pilot — Dashboard Brief

## The scenario
Maya Chen, **Chief Innovation Officer at MeridianCare Health Network** (4 hospitals, 18 clinics in the Pacific Northwest), launched a 12-month Remote Patient Monitoring (RPM) pilot called **Sentinel Health** nine months ago.

The pilot enrolled 250 patients with chronic conditions (Type 2 Diabetes, Hypertension, CHF, COPD) across six partner clinics. Each patient received:
- A connected device (BP cuff, glucometer, smart scale, or pulse oximeter depending on condition)
- A mobile app for symptom & reading logging
- Weekly virtual check-ins with a care coordinator

**Cost: ~$1,800 per patient per year (~$150/month).**

The Board meets in 4 weeks to decide: **scale system-wide (~12,000 eligible patients) or sunset the program.**

## The questions the dashboard must answer
1. **Outcomes.** Is Sentinel reducing ER visits and hospitalizations vs. the 12 months pre-enrollment?
2. **Segmentation.** Which patient segments benefit most — by condition, age band, baseline risk?
3. **Engagement.** Is engagement (readings, app use, completed calls) strong enough to justify scaling? Does engagement correlate with outcomes?
4. **Site performance.** Which of the 6 clinics are succeeding, and which are struggling? Why?
5. **Economics.** Is the $1,800/patient/year cost justified by the avoided ER/hospital utilization?

## Suggested dashboard sections
- **KPI strip at top**: total enrolled, active rate, overall ER reduction %, hospitalization reduction %, avg patient satisfaction, total program cost to date
- **Outcomes panel**: pre-vs-during bar comparison for ER visits and hospitalizations, broken down by condition
- **Site performance**: ranked table or heatmap of the 6 clinics across engagement + outcomes metrics — should make star and struggling sites jump out
- **Engagement-vs-outcomes**: scatter (avg weekly readings on X, ER reduction on Y, sized by risk) to show the correlation
- **Segment cuts**: outcomes by age band, by primary condition, by baseline risk tier
- **Cost-benefit**: estimated avoided ER/hospital costs vs. program cost (use rough US averages — ER visit ~$1,400, hospitalization ~$13,000 — and call out the assumption)
- **Filter row**: clinic site, condition, status — should filter all panels

## Data dictionary (`sentinel_health_pilot.csv`, 250 rows, 26 columns)

| Column | Type | Notes |
|---|---|---|
| `patient_id` | string | Unique ID, P0001–P0250 |
| `enrollment_date` | date | When the patient joined the pilot |
| `days_enrolled` | int | Days from enrollment to snapshot date (2026-05-18) |
| `clinic_site` | string | One of 6 sites |
| `age` | int | 28–92 |
| `gender` | string | Female / Male / Non-binary |
| `primary_condition` | string | Type 2 Diabetes / Hypertension / CHF / COPD |
| `baseline_risk_score` | float | 1.0–10.0, higher = sicker |
| `device_type` | string | BP Monitor / Glucometer / Multi-device / Pulse Oximeter |
| `avg_weekly_readings` | float | Engagement: device readings per week |
| `app_logins_per_month` | int | Engagement: mobile app activity |
| `care_calls_scheduled` | int | Weekly virtual check-ins scheduled |
| `care_calls_completed` | int | …of which completed (completion rate = completed/scheduled) |
| `alerts_triggered` | int | Out-of-range readings flagged to care team |
| `baseline_metric_name` | string | Which clinical metric was tracked (varies by condition) |
| `baseline_metric_value` | float | Value at enrollment (units depend on metric — A1C %, mmHg, kg, SpO2 %) |
| `latest_metric_value` | float | Most recent value — improvement direction depends on metric |
| `er_visits_12mo_pre` | int | ER visits in the 12 months **before** enrollment |
| `er_visits_during_program` | int | ER visits **during** the program |
| `hospitalizations_12mo_pre` | int | Inpatient admits, 12 mo pre |
| `hospitalizations_during_program` | int | Inpatient admits during program |
| `medication_adherence_pct` | int | 0–100 |
| `patient_satisfaction_5pt` | float | 1.0–5.0 |
| `monthly_program_cost_usd` | float | ~$150 with variation |
| `total_cost_to_date_usd` | float | monthly cost × months enrolled |
| `status` | string | Active / Disengaged / Withdrew / Completed |

### Direction-of-improvement caveat for clinical metrics
- **A1C** (Diabetes): lower is better
- **Systolic BP** (Hypertension): lower is better
- **Weight kg** (CHF): modest reduction is better (fluid management)
- **SpO2** (COPD): **higher** is better

Group by `baseline_metric_name` when computing % improvement so the direction is right.

### Useful derived columns to compute
- `er_reduction = er_visits_12mo_pre - er_visits_during_program`
- `hosp_reduction = hospitalizations_12mo_pre - hospitalizations_during_program`
- `call_completion_rate = care_calls_completed / care_calls_scheduled`
- `age_band` e.g. <55 / 55–69 / 70+
- `engagement_tier` based on `avg_weekly_readings` quartiles
- `estimated_savings_usd = er_reduction * 1400 + hosp_reduction * 13000` (call out assumption)
- `net_value_usd = estimated_savings_usd - total_cost_to_date_usd`

## Tech suggestion
Streamlit or Plotly Dash for a quick interactive dashboard; or a static HTML report with Plotly if she wants something to share with the Board. Build with pandas for the data layer.

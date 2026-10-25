import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Auto Insurance Risk Segmentation", layout="wide")
st.title("Auto Insurance Risk Segmentation")
st.caption("French motor insurance data (freMTPL2): 678K policies. Frequency = claims per policy-year; loss cost = claim amount per policy-year (€).")

tiers = pd.read_csv("data/tier_summary.csv")
age = pd.read_csv("data/age_summary.csv")
bm = pd.read_csv("data/bm_summary.csv")
veh = pd.read_csv("data/veh_summary.csv")

ratio = tiers["actual_loss_cost"].iloc[-1] / tiers["actual_loss_cost"].iloc[0]
c1, c2, c3 = st.columns(3)
c1.metric("Policies analyzed", "678,013")
c2.metric("Top vs bottom tier loss cost", f"{ratio:.1f}x")
c3.metric("Highest tier frequency", f"{tiers['actual_frequency'].iloc[-1]:.3f}")

st.subheader("Risk tiers: predicted vs actual loss cost")
tiers["tier"] = tiers["tier"].astype(str)
long = tiers.melt(id_vars="tier", value_vars=["actual_loss_cost", "predicted_loss_cost"],
                  var_name="type", value_name="loss_cost")
fig = px.bar(long, x="tier", y="loss_cost", color="type", barmode="group")
fig.update_xaxes(type="category")
st.plotly_chart(fig, width="stretch")

st.subheader("Claim frequency by customer group")
left, mid, right = st.columns(3)
left.plotly_chart(px.bar(age, x="age_band", y="frequency", title="Driver age"), width="stretch")
mid.plotly_chart(px.bar(bm, x="bonus_malus_band", y="frequency", title="Driving history (BonusMalus)"), width="stretch")
right.plotly_chart(px.bar(veh, x="veh_age_band", y="frequency", title="Vehicle age"), width="stretch")

st.caption("Limitation: analytical exercise, not a production pricing model.")
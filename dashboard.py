import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Maritime Analytics Dashboard", layout="wide")

df = pd.read_csv("data/maritime_master_dataset.csv")

st.title("🚢 Maritime Performance Analytics & Sea-Route Risk Assessment")

# Sidebar filters
vessel_type = st.sidebar.selectbox(
    "Select Vessel Type",
    df["vessel_type"].unique()
)

filtered_df = df[df["vessel_type"] == vessel_type]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Avg Speed (knots)", round(filtered_df["speed_knots"].mean(), 2))
col2.metric("Avg Fuel Used (LPH)", round(filtered_df["fuel_used_lph"].mean(), 2))
col3.metric("Avg Wave Height (m)", round(filtered_df["wave_height_m"].mean(), 2))

# Speed vs Fuel
st.subheader("Speed vs Fuel Consumption")
fig, ax = plt.subplots()
sns.scatterplot(x="speed_knots", y="fuel_used_lph", data=filtered_df, ax=ax)
st.pyplot(fig)

# Submarine Depth vs Speed
if vessel_type == "Submarine":
    st.subheader("Depth vs Speed (Submarine)")
    fig, ax = plt.subplots()
    sns.lineplot(x="depth_m", y="speed_knots", data=filtered_df, ax=ax)
    st.pyplot(fig)

# Route Risk Index
filtered_df["risk_index"] = (
    filtered_df["wave_height_m"] * 0.3 +
    filtered_df["storm_probability"] * 0.3 +
    filtered_df["course_deviation_deg"] * 0.2
)

st.subheader("Sea-Route Risk Index")
st.line_chart(filtered_df["risk_index"])

st.success("Dashboard loaded successfully 🚀")

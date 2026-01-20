import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Maritime Analytics Dashboard", layout="wide")

# -------------------- LOAD DATA --------------------
ship_df = pd.read_csv("ship_specifications.csv")
nav_df = pd.read_csv("navigation_logs.csv")
env_df = pd.read_csv("environmental_conditions.csv")
fuel_df = pd.read_csv("fuel_consumption.csv")
maint_df = pd.read_csv("maintenance_incidents.csv")

# -------------------- MERGE DATA --------------------
df = nav_df.merge(ship_df, on="Vessel_ID", how="left")
df = df.merge(env_df, on=["Vessel_ID", "Timestamp"], how="left")
df = df.merge(fuel_df, on=["Vessel_ID", "Timestamp"], how="left")
df = df.merge(maint_df, on="Vessel_ID", how="left")

# -------------------- SIDEBAR --------------------
st.sidebar.header("Filters")

vessel_type = st.sidebar.multiselect(
    "Select Vessel Type",
    df["Type"].dropna().unique(),
    default=df["Type"].dropna().unique()
)

df = df[df["Type"].isin(vessel_type)]

# -------------------- KPI METRICS --------------------
st.title("🚢 Maritime Performance & Sea-Route Risk Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Speed (knots)", round(df["Speed"].mean(), 2))
col2.metric("Avg Fuel / NM", round(df["Fuel_per_NM"].mean(), 2))
col3.metric("Avg Wave Height", round(df["Wave_Height"].mean(), 2))
col4.metric("Total Incidents", df["Incident_Type"].count())

# -------------------- BAR CHART --------------------
st.subheader("Fuel Consumption by Vessel Type")

fig1, ax1 = plt.subplots()
sns.barplot(data=df, x="Type", y="Fuel_per_NM", ax=ax1)
ax1.set_ylabel("Fuel per Nautical Mile")
st.pyplot(fig1)

# -------------------- LINE CHART --------------------
st.subheader("Speed vs Wave Height")

fig2, ax2 = plt.subplots()
sns.lineplot(data=df, x="Wave_Height", y="Speed", ax=ax2)
ax2.set_xlabel("Wave Height")
ax2.set_ylabel("Speed (knots)")
st.pyplot(fig2)

# -------------------- SCATTER PLOT --------------------
st.subheader("Fuel Consumption vs Load Weight")

fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x="Load_Weight", y="Fuel_per_NM", hue="Type", ax=ax3)
st.pyplot(fig3)

# -------------------- HEATMAP --------------------
st.subheader("Correlation Heatmap")

numeric_df = df.select_dtypes(include=np.number)
fig4, ax4 = plt.subplots(figsize=(10,6))
sns.heatmap(numeric_df.corr(), cmap="coolwarm", ax=ax4)
st.pyplot(fig4)

# -------------------- RISK MODEL --------------------
st.subheader("Sea Route Risk Assessment")

df["Environmental_Risk"] = (
    0.4 * df["Wave_Height"] +
    0.3 * df["Wind_Speed"] +
    0.3 * df["Storm_Probability"]
)

df["Route_Risk"] = np.where(
    df["Environmental_Risk"] > df["Environmental_Risk"].quantile(0.66),
    "High",
    np.where(
        df["Environmental_Risk"] > df["Environmental_Risk"].quantile(0.33),
        "Medium",
        "Low"
    )
)

risk_counts = df["Route_Risk"].value_counts()

fig5, ax5 = plt.subplots()
risk_counts.plot(kind="bar", ax=ax5)
ax5.set_ylabel("Route Count")
st.pyplot(fig5)

# -------------------- DATA TABLE --------------------
st.subheader("Sample Data View")
st.dataframe(df.head(20))

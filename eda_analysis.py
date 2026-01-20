import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/maritime_master_dataset.csv")
sns.set_theme(style="whitegrid")

# 1. BAR CHART: Maintenance Intensity
sns.barplot(x="vessel_id", y="repair_hours", data=df, palette="magma")
plt.title("Maintenance Repair Hours by Vessel")
plt.show()

# 2. HISTOGRAM: Speed Distribution
sns.histplot(df["speed_knots"], bins=5, kde=True, color="teal")
plt.title("Distribution of Vessel Speeds")
plt.show()

# 3. TREE MAP (Pie Chart): Fleet Composition
df['vessel_type'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title("Fleet Composition by Vessel Type")
plt.ylabel("")
plt.show()

# 4. SCATTER: Speed vs Wave Height
sns.scatterplot(x="wave_height_m", y="speed_knots", hue="vessel_type", data=df, s=100)
plt.title("Speed vs Wave Height")
plt.show()

# 5. LINE: Submarine Depth vs Speed
sub_df = df[df["vessel_type"] == "Submarine"]
if not sub_df.empty:
    sns.lineplot(x="depth_m", y="speed_knots", marker="o", data=sub_df)
    plt.title("Submarine Depth vs Speed")
    plt.show()

# 6. HEATMAP: Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes("number").corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("✅ EDA analysis completed with Bar, Histogram, and Tree Map.")

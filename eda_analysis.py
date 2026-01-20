import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/maritime_master_dataset.csv")

# Speed vs Wave Height
sns.scatterplot(x="wave_height_m", y="speed_knots", data=df)
plt.title("Speed vs Wave Height")
plt.show()

# Fuel Consumption vs Load
sns.scatterplot(x="load_weight_tons", y="fuel_used_lph", data=df)
plt.title("Fuel Consumption vs Load Weight")
plt.show()

# Submarine Depth vs Speed
sub_df = df[df["vessel_type"] == "Submarine"]
sns.lineplot(x="depth_m", y="speed_knots", data=sub_df)
plt.title("Submarine Depth vs Speed")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes("number").corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("✅ EDA analysis completed.")

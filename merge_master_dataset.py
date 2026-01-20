import pandas as pd

ship_df = pd.read_csv("data/processed/ship_specifications_clean.csv")
nav_df = pd.read_csv("data/processed/navigation_logs_clean.csv")
env_df = pd.read_csv("data/processed/environmental_conditions_clean.csv")
fuel_df = pd.read_csv("data/processed/fuel_consumption_clean.csv")
maint_df = pd.read_csv("data/processed/maintenance_logs_clean.csv")

# Merge datasets
master_df = nav_df.merge(ship_df, on="vessel_id", how="left")
master_df = master_df.merge(env_df, on=["timestamp", "latitude", "longitude"], how="left")
master_df = master_df.merge(fuel_df, on=["vessel_id", "timestamp"], how="left")
master_df = master_df.merge(maint_df, on="vessel_id", how="left")

# Save master dataset
master_df.to_csv("data/maritime_master_dataset.csv", index=False)

print("✅ Maritime master dataset created.")

import pandas as pd

# Load raw datasets
ship_df = pd.read_csv("data/raw/ship_specifications.csv")
nav_df = pd.read_csv("data/raw/navigation_logs.csv")
env_df = pd.read_csv("data/raw/environmental_conditions.csv")
fuel_df = pd.read_csv("data/raw/fuel_consumption.csv")
maint_df = pd.read_csv("data/raw/maintenance_logs.csv")

def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(method="ffill")
    return df

ship_df = clean_data(ship_df)
nav_df = clean_data(nav_df)
env_df = clean_data(env_df)
fuel_df = clean_data(fuel_df)
maint_df = clean_data(maint_df)

# Save cleaned datasets
ship_df.to_csv("data/processed/ship_specifications_clean.csv", index=False)
nav_df.to_csv("data/processed/navigation_logs_clean.csv", index=False)
env_df.to_csv("data/processed/environmental_conditions_clean.csv", index=False)
fuel_df.to_csv("data/processed/fuel_consumption_clean.csv", index=False)
maint_df.to_csv("data/processed/maintenance_logs_clean.csv", index=False)

print("✅ Data cleaning completed successfully.")

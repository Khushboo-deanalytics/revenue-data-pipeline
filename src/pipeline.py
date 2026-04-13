from data_generator import generate_data
# import data_generator
from data_cleaner import clean_data
import pandas as pd
import os

# Optional: import analytics functions
from analytics import (
    revenue_by_product,
    monthly_revenue,
    top_customers_by_spend,
    top_customers_by_frequency
)


def run_pipeline():

    print("🚀 Starting pipeline...")

    # Step 1: Generate Data
    print("Step 1: Generating data...")
    df = generate_data()
    # df = data_generator.generate_data()

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/orders.csv", index=False)

    print("Raw data saved.")

    # Step 2: Clean Data
    print("Step 2: Cleaning data...")
    clean_data()

    print("Data cleaned.")

    # Step 3: Analytics
    print("Step 3: Running analytics...")

    df_clean = pd.read_csv("data/processed/clean_orders.csv")
    df_clean["booking_date"] = pd.to_datetime(df_clean["booking_date"], errors="coerce")

    revenue_by_product(df_clean)
    monthly_revenue(df_clean)
    top_customers_by_spend(df_clean)
    top_customers_by_frequency(df_clean)

    print("Analytics completed.")

    print("✅ Pipeline finished successfully!")


if __name__ == "__main__":
    run_pipeline()
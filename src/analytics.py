import pandas as pd
import os

INPUT_PATH = "data/processed/clean_orders.csv"
OUTPUT_DIR = "data/analytics"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def revenue_by_product(df):
    result = df.groupby("product")["price"].sum().reset_index()
    result.to_csv(f"{OUTPUT_DIR}/revenue_by_product.csv", index=False)
    print("Saved revenue_by_product")


def monthly_revenue(df):
    df["month"] = df["booking_date"].dt.to_period("M").astype(str)
    result = df.groupby("month")["price"].sum().reset_index()
    result.to_csv(f"{OUTPUT_DIR}/monthly_revenue.csv", index=False)
    print("Saved monthly_revenue")


def top_customers_by_spend(df):
    result = df.groupby("customer_name")["price"].sum().reset_index()
    result = result.sort_values(by="price", ascending=False)
    result.to_csv(f"{OUTPUT_DIR}/top_customers_by_spend.csv", index=False)
    print("Saved top_customers_by_spend")


def top_customers_by_frequency(df):
    result = df.groupby("customer_name")["order_id"].count().reset_index()
    result = result.sort_values(by="order_id", ascending=False)
    result.to_csv(f"{OUTPUT_DIR}/top_customers_by_frequency.csv", index=False)
    print("Saved top_customers_by_frequency")


def main():
    df = pd.read_csv(INPUT_PATH)

    # Convert booking_date again (safety)
    df["booking_date"] = pd.to_datetime(df["booking_date"], errors="coerce")

    revenue_by_product(df)
    monthly_revenue(df)
    top_customers_by_spend(df)
    top_customers_by_frequency(df)


if __name__ == "__main__":
    main()
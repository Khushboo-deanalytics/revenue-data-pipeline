import pandas as pd

# Allowed product mapping
PRODUCT_MAPPING = {
    "flight": "Flight",
    "fligt": "Flight",
    "FLIGHT": "Flight",
    "hotel": "Hotel",
    "htel": "Hotel",
    "car": "Car",
    "car ": "Car"
}


def clean_data():

    # Step 1: Read raw data
    df = pd.read_csv("data/orders.csv")

    print("Initial rows:", len(df))

    # Step 2: Remove duplicates
    df = df.drop_duplicates(subset=["order_id"])

    print("After removing duplicates:", len(df))

    # Step 3: Standardize product names
    df["product"] = df["product"].astype(str).str.strip()
    df["product"] = df["product"].str.lower()
    df["product"] = df["product"].map(PRODUCT_MAPPING).fillna("Unknown")

    # Step 4: Convert price to numeric
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Step 5: Fix negative prices + flag
    df["is_price_corrected"] = df["price"] < 0
    df["price"] = df["price"].abs()

    # Step 6: Handle missing city
    df["city"] = df["city"].fillna("Unknown")

    # Step 7: Convert booking_date
    df["booking_date"] = pd.to_datetime(df["booking_date"], errors="coerce")

    # Step 8: Flag future bookings
    today = pd.Timestamp.today()
    df["is_future_booking"] = df["booking_date"] > today

    # Step 9: Save cleaned data
    output_path = "data/processed/clean_orders.csv"
    df.to_csv(output_path, index=False)

    print("Cleaned data saved at:", output_path)


if __name__ == "__main__":
    clean_data()
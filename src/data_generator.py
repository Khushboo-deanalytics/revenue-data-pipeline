# from faker import Faker
# import pandas as pd
# import random

# fake = Faker()

# def generate_orders(n=1000):
#     data = []

#     for _ in range(n):
#         data.append({
#             "order_id": fake.uuid4(),
#             "customer_name": fake.name(),
#             "city": fake.city(),
#             "product": random.choice(["Flight", "Hotel", "Car"]),
#             "price": random.randint(100, 2000),
#             "booking_date": fake.date_this_year()
#         })

#     return pd.DataFrame(data)


# if __name__ == "__main__":
#     if __name__ == "__main__":
#         print("Script started")

#         df = generate_orders(1000)

#         print("Generated rows:", len(df))

#         df.to_csv("data/orders.csv", index=False)

#         print("Data generated!")

import pandas as pd
import random
from datetime import datetime, timedelta

# Config
NUM_RECORDS = 1000

products = ["Flight", "Hotel", "Car"]
cities = ["Delhi", "Mumbai", "Bangalore", "Chennai"]
bad_product_names = ["fligt", "htel", "car ", "FLIGHT"]

def random_date():
    start_date = datetime(2023, 1, 1)
    return start_date + timedelta(days=random.randint(0, 800))

def generate_data():
    data = []

    for i in range(NUM_RECORDS):
        order_id = i + 1
        customer_id = f"C{random.randint(1, 100)}"
        product = random.choice(products)
        price = round(random.uniform(100, 1000), 2)
        city = random.choice(cities)
        booking_date = random_date()

        data.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "product": product,
            "price": price,
            "city": city,
            "booking_date": booking_date
        })

    df = pd.DataFrame(data)

    # -----------------------
    # Introduce Errors
    # -----------------------

    # 1. Duplicate rows
    # df = pd.concat([df, df.sample(50)])
    df = pd.concat([df, df.sample(50)], ignore_index=True)

    # 2. Missing values
    df.loc[df.sample(50).index, "city"] = None

    # 3. Misspelled products
    df.loc[df.sample(50).index, "product"] = random.choice(bad_product_names)

    # 4. Negative prices
    df.loc[df.sample(30).index, "price"] = -100

    # 5. Future dates
    future_date = datetime.now() + timedelta(days=365)
    df.loc[df.sample(30).index, "booking_date"] = future_date

    # 6. Mixed date formats
    df["booking_date"] = df["booking_date"].astype(str)
    df.loc[df.sample(50).index, "booking_date"] = "03/15/2025"

    # 7. Price as string
    # df.loc[df.sample(50).index, "price"] = df["price"].astype(str)
    df["price"] = df["price"].astype(object)
    sample_idx = df.sample(50).index
    df.loc[sample_idx, "price"] = df.loc[sample_idx, "price"].astype(str)

    return df


def main():
    df = generate_data()

    output_path = "data/raw/orders.csv"
    df.to_csv(output_path, index=False)

    print(f"Data generated at {output_path}")


if __name__ == "__main__":
    main()
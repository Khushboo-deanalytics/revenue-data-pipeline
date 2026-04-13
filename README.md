# 📊 Revenue Data Pipeline (End-to-End Data Engineering Project)

## 🚀 Overview

This project simulates a real-world data engineering pipeline for a travel booking platform.

It covers the full lifecycle of data:
- Data generation (simulating messy real-world data)
- Data cleaning and standardization
- Analytical dataset creation

The goal is to demonstrate how raw, inconsistent data can be transformed into reliable business insights.

---

## 🧩 Problem Statement

In real-world systems, raw data often contains:
- Missing values
- Duplicate records
- Incorrect formats
- Data inconsistencies

This project builds a pipeline to clean and process such data efficiently.

---

## 🏗️ Architecture
# 📊 Revenue Data Pipeline (End-to-End Data Engineering Project)

## 🚀 Overview

This project simulates a real-world data engineering pipeline for a travel booking platform.

It covers the full lifecycle of data:
- Data generation (simulating messy real-world data)
- Data cleaning and standardization
- Analytical dataset creation

The goal is to demonstrate how raw, inconsistent data can be transformed into reliable business insights.

---

## 🧩 Problem Statement

In real-world systems, raw data often contains:
- Missing values
- Duplicate records
- Incorrect formats
- Data inconsistencies

This project builds a pipeline to clean and process such data efficiently.

---

## 🏗️ Architecture
Data Generation → Raw Data → Data Cleaning → Processed Data → Analytics


---

## ⚙️ Tech Stack

- Python
- Pandas
- CSV (simulating data lake)
- Modular pipeline design

---

## 📂 Project Structure
data/
raw/
processed/
analytics/

src/
data_generator.py
data_cleaner.py
analytics.py
pipeline.py


---

## 🔄 Pipeline Steps

### 1. Data Generation
- Synthetic booking data created
- Includes intentional issues:
  - duplicates
  - missing values
  - wrong formats
  - negative prices

---

### 2. Data Cleaning
- Removed duplicate records
- Standardized product names
- Handled missing values
- Converted data types
- Added data quality flags:
  - `is_price_corrected`
  - `is_future_booking`

---

### 3. Analytics Layer

Generated business insights:

- Revenue by product
- Monthly revenue trends
- Top customers by spend
- Top customers by frequency

---

## 📊 Sample Outputs

- `revenue_by_product.csv`
- `monthly_revenue.csv`
- `top_customers_by_spend.csv`
- `top_customers_by_frequency.csv`

---

## 🎯 Key Learnings

- Handling messy real-world data
- Designing modular data pipelines
- Data cleaning strategies
- Building analytics-ready datasets

---

## 🔮 Future Improvements

- Integration with cloud (GCP / BigQuery)
- Pipeline orchestration (Airflow)
- Dashboard layer (Tableau / Power BI)
- ML-based forecasting

---

## 👩‍💻 About Me

I transitioned from SAP Finance to Data Engineering and built this project to simulate real-world data challenges.

I enjoy solving messy data problems and building structured pipelines.

# Databricks notebook source
import os

from pyspark.sql import functions as F

# COMMAND ----------

dbutils.widgets.text("timestamp", "2023-04-01")

timestamp = dbutils.widgets.get("timestamp")

# COMMAND ----------

env = os.environ["ENV"]
feature_table_name = f"{env}.mlops_demo.customer_features"

# COMMAND ----------

df_final = (
    spark.table(f"{env}.mlops_demo.silver_customer")
    .drop("ChurnLabel")
    .withColumn("timestamp", F.lit(timestamp).cast("timestamp"))
)
# display(df_final)

# COMMAND ----------

metadata = {
    "table": "features",
    "category": "",
    "features": {
        "Count": {"description": "Description Count"},
        "Country": {"description": "Description Country"},
        "State": {"description": "Description State"},
        "City": {"description": "Description City"},
        "ZipCode": {"description": "Description ZipCode"},
        "LatLong": {"description": "Description LatLong"},
        "Latitude": {"description": "Description Latitude"},
        "Longitude": {"description": "Description Longitude"},
        "Gender": {"description": "Description Gender"},
        "SeniorCitizen": {"description": "Description SeniorCitizen"},
        "Partner": {"description": "Description Partner"},
        "Dependents": {"description": "Description Dependents"},
        "TenureMonths": {"description": "Description TenureMonths"},
        "PhoneService": {"description": "Description PhoneService"},
        "MultipleLines": {"description": "Description MultipleLines"},
        "InternetService": {"description": "Description InternetService"},
        "OnlineSecurity": {"description": "Description OnlineSecurity"},
        "OnlineBackup": {"description": "Description OnlineBackup"},
        "DeviceProtection": {"description": "Description DeviceProtection"},
        "TechSupport": {"description": "Description TechSupport"},
        "StreamingTV": {"description": "Description StreamingTV"},
        "StreamingMovies": {"description": "Description StreamingMovies"},
        "Contract": {"description": "Description Contract"},
        "PaperlessBilling": {"description": "Description PaperlessBilling"},
        "PaymentMethod": {"description": "Description PaymentMethod"},
        "MonthlyCharges": {"description": "Description MonthlyCharges"},
        "TotalCharges": {"description": "Description TotalCharges"},
        "ChurnValue": {"description": "Description ChurnValue"},
        "ChurnScore": {"description": "Description ChurnScore"},
        "CLTV": {"description": "Description CLTV"},
        "ChurnReason": {"description": "Description ChurnReason"},
    },
}


# Databricks notebook source

from pyspark.sql import functions as F
from datetime import datetime

# Parameters
dbutils.widgets.text("env", "dev")
dbutils.widgets.text("run_date", datetime.today().strftime('%Y-%m-%d'))

env = dbutils.widgets.get("env")
run_date = dbutils.widgets.get("run_date")

print(f"Running Silver Layer | env={env} | date={run_date}")

# Simulate reading bronze
df_bronze = spark.range(10)

# Transform
df_silver = (
    df_bronze
    .withColumn("sales_amount", F.lit(100.0))
    .withColumn("processed_ts", F.current_timestamp())
)

display(df_silver)

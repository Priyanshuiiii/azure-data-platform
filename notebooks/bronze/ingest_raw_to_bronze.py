# Databricks notebook source
from pyspark.sql import functions as F
from datetime import datetime

# Parameters
dbutils.widgets.text("env", "dev")
env = dbutils.widgets.get("env")

print(f"Running Bronze pipeline in {env}")

# Simulate raw ingestion
df = spark.range(10)

df = df.withColumn("ingestion_time", F.current_timestamp())

display(df)

# Databricks notebook source

dbutils.widgets.text("timestamp", "2020-12-12")

# COMMAND ----------

# notebook must contain dataframe 'df_final' which contains features
df_final = __your_logic__

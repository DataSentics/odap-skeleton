# Databricks notebook source
# MAGIC %run ./init/odap

# COMMAND ----------

# MAGIC %sql
# MAGIC create widget text timestamp default "2020-12-12"

# COMMAND ----------

from odap.segment_factory.orchestrate import orchestrate

orchestrate()

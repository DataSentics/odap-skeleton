# Databricks notebook source
# MAGIC %run ../init/odap

# COMMAND ----------

# MAGIC %sql
# MAGIC create widget text timestamp default "2023-01-01"

# COMMAND ----------

from odap.feature_factory.widgets import create_notebooks_widget

create_notebooks_widget()

# COMMAND ----------

from odap.feature_factory.orchestrate import orchestrate

orchestrate()

# COMMAND ----------

# Uncomment if you want to use latest snapshot table and have filled the ids.table configuration in config.yaml
# from odap.feature_factory.orchestrate import calculate_latest_table

# calculate_latest_table()

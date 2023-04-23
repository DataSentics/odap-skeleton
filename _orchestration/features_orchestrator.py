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

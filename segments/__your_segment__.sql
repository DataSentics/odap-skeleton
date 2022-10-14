-- Databricks notebook source
create widget text timestamp default "2020-12-12"

-- COMMAND ----------

select
  __entity_id_column__
from
  hive_metastore.odap_features.__entity__
where
  -- TODO: __your_logic__

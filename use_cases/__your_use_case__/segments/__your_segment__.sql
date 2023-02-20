-- Databricks notebook source

select
  __entity_id_column__
from
  hive_metastore.odap_features_your_entity_name.latest
where
  true
  -- TODO: __your_logic__

# Databricks notebook source
import dlt
import pyspark.sql.functions as F


# COMMAND ----------

@dlt.table(name="silverS")
def silverS():
   df=dlt.read("bronzeS")
   cleaned_df=(
       df
       .dropDuplicates()
       .filter(F.col("student_id").isNotNull())
   )
   return cleaned_df
# Databricks notebook source
import dlt
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

@dlt.table(name="bronzeS")
def bronzeS():
    return(
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format","csv")
        .option("header","true")
        .option("inferschema","true")
        .load("/Volumes/practice/student/studentv/studentr/")
        .withColumn("ingestion_time",current_timestamp())
    )
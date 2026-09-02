# Databricks notebook source
import dlt
import pyspark.sql.functions as F

# COMMAND ----------



# COMMAND ----------

@dlt.table(name="studentsdoinparttimejob")
def studentsdoinparttimejob():
    return(
        dlt.read("silverS")
        .groupBy("part_time_job","internet_access")
        .agg(
            F.count("student_id").alias ("total_student"),
            F.count("internet_access").alias("total")
        )
    )
@dlt.table(name="avg_study_time_hours")
def avg_study_time_hours():
    return(
        dlt.read("silverS")
        .agg(
            F.avg("study_time_hours").alias("avg_study_hours"),
            F.avg("final_exam_score").alias("avg_marks")
        )
    )


@dlt.table(name="parentseducation")
def parental_education():
    return(
        dlt.read("silverS")
        .groupBy("parental_education")
        .agg(
            F.count("student_id").alias("total_students"),
            F.count("parental_education").alias("total_parental_education_count")
        )
    )
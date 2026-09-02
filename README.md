#  student-performance-dlt-pipeline

**End-to-end ETL pipeline on the Student Performance dataset using Databricks Delta Live Tables (DLT), built on the Medallion Architecture (Bronze → Silver → Gold).**

##  Architecture

```
┌─────────────┐      ┌─────────────┐      ┌──────────────────────────────┐
│   Bronze      ───▶    Silver      ───▶             Gold               
│ (Raw Ingest)        (Cleaned)             (Business Aggregates)        
└─────────────┘      └─────────────┘      └──────────────────────────────┘
    bronzeS              silverS            studentsdoinparttimejob
  (CSV → Delta,       (dedup, null-        avg_study_time_hours
   Autoloader)         filtered on          parentseducation
                        student_id)
```

| Layer | Table(s) | Purpose |
|---|---|---|
| **Bronze** | `bronzeS` | Raw ingestion from CSV via Autoloader, with ingestion timestamp |
| **Silver** | `silverS` | Deduplicated, filtered on non-null `student_id` |
| **Gold** | `studentsdoinparttimejob`, `avg_study_time_hours`, `parentseducation` | Business-level aggregations |

---

##  Bronze Layer — Raw Ingestion

Ingests raw student performance CSV data via Databricks Autoloader, tagging each record with an ingestion timestamp.
---

##  Silver Layer — Cleaning

## Gold Layer — Business Aggregations

## ▶️ How to Run

1. Upload pipeline notebooks/files to a Databricks Repo.
2. Upload `student_performance_dataset.csv` to the Volume path referenced in `bronzeS` (`/Volumes/practice/student/studentv/studentr/`).
3. Create a **Delta Live Tables Pipeline** in Databricks pointing to these notebooks.
4. Run the pipeline (Triggered/Continuous).
5. Query Gold tables via Databricks SQL or connect to a BI dashboard.

---

##  Tech Stack
- Databricks Delta Live Tables (DLT)
- PySpark / `pyspark.sql.functions`
- Delta Lake
- Medallion Architecture (Bronze / Silver / Gold)

---

##  Dataset Source
Student Performance dataset — ~1,000 students with academic, lifestyle, and demographic attributes.

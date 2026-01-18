# Day 10 – Performance Optimization in Databricks

## Objective
The goal of Day 10 was to understand and apply performance optimization techniques
to improve query execution speed in Databricks using Delta Lake.

This focused on identifying bottlenecks, optimizing data layout, and measuring
performance improvements through benchmarking.

---

## Dataset
The optimization was performed on the `vrinda_store_data` dataset
registered under the `databricks_challenge` catalog.

---

## What Was Implemented

### 1. Query Execution Plan Analysis
- Used `explain()` to analyze how Spark executes queries
- Identified full table scans and filter behavior before optimization

### 2. Table Partitioning
- Created a partitioned version of the table to reduce data scanned per query
- Partitioning strategy was chosen based on commonly filtered columns

### 3. Delta Lake Optimization
- Applied `OPTIMIZE` to compact small files
- Used `ZORDER` on frequently filtered columns to improve data skipping

### 4. Caching
- Cached frequently accessed tables to speed up repeated queries

### 5. Benchmarking
- Measured query execution time before and after optimization
- Observed improved performance after applying partitioning and ZORDER
- Validated optimizations using real query workloads

---

## Key Learnings
- Performance optimization is highly dependent on query patterns
- Partitioning is effective when queries leverage partition columns
- ZORDER improves performance for selective filters on non-partition columns
- Benchmarking is essential to validate the impact of optimizations
- Optimizations should be applied based on usage, not assumptions

---

## Tools & Technologies
- Databricks Community Edition
- Apache Spark (PySpark)
- Delta Lake
- Databricks SQL

---

## Conclusion
This exercise demonstrated how proper data layout and Delta Lake optimizations
can significantly improve query performance when applied thoughtfully and
validated through benchmarking.

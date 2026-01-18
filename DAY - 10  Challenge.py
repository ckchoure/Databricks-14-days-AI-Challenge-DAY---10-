# Databricks notebook source
# MAGIC %md
# MAGIC # Task 01:- Analyze query plans

# COMMAND ----------

# Load Vrinda Store Data
store_df = spark.table("databricks_challenge.vrinda_store.vrinda_store_data")

# sample analytical query
filtered_df = store_df.filter(store_df.Channel == "Ajio")

# check execution plan
filtered_df.explain(True)

# COMMAND ----------

# MAGIC %md
# MAGIC # Task 02:- Partition large tables

# COMMAND ----------

# Repartition and write table partitioned by Date
store_df.write \
    .format("delta") \
    .mode("overwrite") \
    .partitionBy("Date") \
    .saveAsTable("databricks_challenge.vrinda_store.vrinda_store_data_partitioned")

# COMMAND ----------

# MAGIC %md
# MAGIC # Task 03:- Apply ZORDER

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC OPTIMIZE databricks_challenge.vrinda_store.vrinda_store_data_partitioned
# MAGIC ZORDER BY (Status, Channel, Month);

# COMMAND ----------

# MAGIC %md
# MAGIC # Task 04:- Benchmark improvements

# COMMAND ----------

# Query on non-optimized table

import time
start_time = time.time()
spark.table("databricks_challenge.vrinda_store.vrinda_store_data") \
    .filter("Category = 'kurta'") \
    .count()
print(f"Elapsed time: {time.time() - start_time} seconds")

# COMMAND ----------

# Query on optimized table

import time
start_time = time.time()
spark.table("databricks_challenge.vrinda_store.vrinda_store_data_partitioned") \
    .filter("Category = 'kurta'") \
    .count()
print(f"Elapsed time: {time.time() - start_time} seconds")
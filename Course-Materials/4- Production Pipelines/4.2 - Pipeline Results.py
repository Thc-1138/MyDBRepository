# Databricks notebook source
files = dbutils.fs.ls("dbfs:/pipelines/ac4b22df-5abf-42dc-a79b-0273afabce10")
display(files)

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/pipelines/ac4b22df-5abf-42dc-a79b-0273afabce10/system/events")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`dbfs:/pipelines/ac4b22df-5abf-42dc-a79b-0273afabce10/system/events`

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/pipelines/ac4b22df-5abf-42dc-a79b-0273afabce10/tables")
display(files)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo_bookstore_dlt_db.cn_daily_customer_books

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo_bookstore_dlt_db.fr_daily_customer_books

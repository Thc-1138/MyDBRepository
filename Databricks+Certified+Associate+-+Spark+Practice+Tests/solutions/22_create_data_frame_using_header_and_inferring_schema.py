# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Create Spark Data Frame using Header and Inferring Schema
# MAGIC
# MAGIC Use the files in dbfs to create Spark Data Frame using Header and Inferring Schema.
# MAGIC * The files are under `dbfs:/public/udemy_tech`
# MAGIC * Preview data using `spark.read.text` to understand characteristics of data.
# MAGIC * Use appropriate key word arguments and API to create Data Frame for the data in the files under `dbfs:/public/udemy_tech`

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Step 1: Preview Files

# COMMAND ----------

# MAGIC %fs ls /public/udemy_tech

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Step 2: Solution
# MAGIC
# MAGIC Develop the required logic in the below using appropriate key word arguments. Also, make sure to log the code snippets used to perform the analysis.

# COMMAND ----------

raw_data = spark.read.text('/public/udemy_tech')

# COMMAND ----------

display(raw_data)

# COMMAND ----------

udemy_data = spark.read.csv('/public/udemy_tech/', header=True, inferSchema=True)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Step 3: Validation
# MAGIC
# MAGIC Run below cells to perform the validation.

# COMMAND ----------

display(udemy_data)

# COMMAND ----------

udemy_data.count() # 21

# COMMAND ----------

udemy_data.dtypes # Output should be as below

# [('course_id', 'int'),
#  ('course_name', 'string'),
#  ('suitable_for', 'string'),
#  ('enrollment', 'int'),
#  ('stars', 'double'),
#  ('number_of_ratings', 'int')]

# COMMAND ----------



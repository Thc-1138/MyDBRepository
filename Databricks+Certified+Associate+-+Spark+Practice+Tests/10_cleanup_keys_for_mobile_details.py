# Databricks notebook source
# MAGIC %md
# MAGIC ## Cleanup Spark Data Frame Columns for mobile details
# MAGIC
# MAGIC Develop logic to remove **mobile** from the column names in the Data Frame.

# COMMAND ----------

mobile_details = [{'mobile_company': 'Apple',
  'mobile_model': 'Iphone 12',
  'mobile_ram': 4,
  'mobile_storage': 256,
  'mobile_os': 'iOS'},
 {'mobile_company': 'Xiaomi',
  'mobile_model': 'Redmi 9',
  'mobile_ram': 4,
  'mobile_storage': 64,
  'mobile_os': 'android'},
 {'mobile_company': 'One plus',
  'mobile_model': 'One plus 9R',
  'mobile_ram': 6,
  'mobile_storage': 128,
  'mobile_os': 'android'},
 {'mobile_company': 'Samsung',
  'mobile_model': 'Galaxy M32',
  'mobile_ram': 4,
  'mobile_storage': 64,
  'mobile_os': 'android'},
 {'mobile_company': 'Xiaomi',
  'mobile_model': 'Redmi note 10 pro',
  'mobile_ram': 8,
  'mobile_storage': 128,
  'mobile_os': 'android'},
 {'mobile_company': 'One plus',
  'mobile_model': 'One plus Nord',
  'mobile_ram': 4,
  'mobile_storage': 128,
  'mobile_os': 'android'},
 {'mobile_company': 'Apple',
  'mobile_model': 'Iphone X',
  'mobile_ram': 4,
  'mobile_storage': 256,
  'mobile_os': 'android'},
 {'mobile_company': 'Oppo',
  'mobile_model': 'Oppo A31',
  'mobile_ram': 4,
  'mobile_storage': 64,
  'mobile_os': 'iOS'}]

# COMMAND ----------

mobile_details_df = spark.createDataFrame(mobile_details)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1: Preview the data
# MAGIC * Let us first preview the data.

# COMMAND ----------

display(mobile_details_df)

# COMMAND ----------

mobile_details_df.count()

# COMMAND ----------

mobile_details_df.columns

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Provide the solution
# MAGIC Now come up with the solution by developing the required logic. Once the logic is developed, go to the next step to take care of the validation.

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC Run below cells for validation.

# COMMAND ----------

display(mobile_details_df_new)

# COMMAND ----------

mobile_details_df_new.columns # ['company', 'model', 'os', 'ram', 'storage']

# COMMAND ----------



# Databricks notebook source
# MAGIC %md
# MAGIC ## Filter for mobiles by RAM and Storage
# MAGIC
# MAGIC Develop a function to get mobile details for given specifications such as RAM and storage from a Spark Data Frame.
# MAGIC * The input data will be a Data Frame with mobile phone specifications.
# MAGIC * The output should contains mobiles based up on the given ram and storage.
# MAGIC * The function should take 3 arguments - list of mobile details, RAM as well as storage.
# MAGIC * The output should be in form of list of dicts. It should be sorted in the ascending order by company followed by model.

# COMMAND ----------

mobile_details = [{'company': 'Apple',
  'model': 'Iphone 12',
  'ram': 4,
  'storage': 256,
  'os': 'iOS'},
 {'company': 'Xiaomi',
  'model': 'Redmi 9',
  'ram': 4,
  'storage': 64,
  'os': 'android'},
 {'company': 'One plus',
  'model': 'One plus 9R',
  'ram': 6,
  'storage': 128,
  'os': 'android'},
 {'company': 'Samsung',
  'model': 'Galaxy M32',
  'ram': 4,
  'storage': 64,
  'os': 'android'},
 {'company': 'Xiaomi',
  'model': 'Redmi note 10 pro',
  'ram': 8,
  'storage': 128,
  'os': 'android'},
 {'company': 'One plus',
  'model': 'One plus Nord',
  'ram': 4,
  'storage': 128,
  'os': 'android'},
 {'company': 'Apple',
  'model': 'Iphone X',
  'ram': 4,
  'storage': 256,
  'os': 'android'},
 {'company': 'Oppo',
  'model': 'Oppo A31',
  'ram': 4,
  'storage': 64,
  'os': 'iOS'}]

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

# MAGIC %md
# MAGIC ### Step 2: Provide the solution
# MAGIC Now come up with the solution by developing the required logic. Once the function is developed, go to the next step to take care of the validation.

# COMMAND ----------

from pyspark.sql.functions import col

def get_mobile_details(mobile_details_df, ram, storage):
    # your code should go hers
    mobiles_filtered = mobile_details_df. \
        filter((col('ram') == ram) & (col('storage') == storage)). \
        orderBy('company', 'model')
    return mobiles_filtered

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Here is the expected output.
# MAGIC
# MAGIC ```python
# MAGIC [{'company': 'Oppo',
# MAGIC   'model': 'Oppo A31',
# MAGIC   'ram': 4,
# MAGIC   'storage': 64,
# MAGIC   'os': 'iOS'},
# MAGIC  {'company': 'Samsung',
# MAGIC   'model': 'Galaxy M32',
# MAGIC   'ram': 4,
# MAGIC   'storage': 64,
# MAGIC   'os': 'android'},
# MAGIC  {'company': 'Xiaomi',
# MAGIC   'model': 'Redmi 9',
# MAGIC   'ram': 4,
# MAGIC   'storage': 64,
# MAGIC   'os': 'android'}]
# MAGIC ```

# COMMAND ----------

mobiles_by_ram_and_storage = get_mobile_details(mobile_details_df, 4, 64)

# COMMAND ----------

display(mobiles_by_ram_and_storage)

# COMMAND ----------

mobiles_by_ram_and_storage.count() # 3

# COMMAND ----------



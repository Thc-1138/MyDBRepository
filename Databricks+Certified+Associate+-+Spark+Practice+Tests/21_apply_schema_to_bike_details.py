# Databricks notebook source
# MAGIC %md
# MAGIC ## Create Data Frame to bike details using StructType
# MAGIC
# MAGIC Develop a fuction to apply schema while creating the Spark Data Frame using Spark StructType.
# MAGIC * Here are the details of the columns
# MAGIC
# MAGIC |Column Name|Data Type|
# MAGIC |-----------|---------|
# MAGIC |name|string|
# MAGIC |selling_price|int|
# MAGIC |year|int|
# MAGIC |seller_type|string|
# MAGIC |owner|string|
# MAGIC |km_driven|int|

# COMMAND ----------

bike_details = [('Royal Enfield Classic 350', 175000, 2019, 'Individual', '1st owner', 350),
 ('Honda Dio', 45000, 2017, 'Individual', '1st owner', 5650),
 ('Royal Enfield Classic Gunmetal Grey', 150000, 2018, 'Individual', '1st owner', 12000),
 ('Yamaha Fazer FI V 2.0 [2016-2018]', 65000, 2015, 'Individual', '1st owner', 23000),
 ('Yamaha SZ [2013-2014]', 20000, 2011, 'Individual', '2nd owner', 21000),
 ('Honda CB Twister', 18000, 2010, 'Individual', '1st owner', 60000),
 ('Honda CB Hornet 160R', 78500, 2018, 'Individual', '1st owner', 17000),
 ('Royal Enfield Bullet 350 [2007-2011]', 180000, 2008, 'Individual', '2nd owner', 39000),
 ('Hero Honda CBZ extreme', 30000, 2010, 'Individual', '1st owner', 32000),
 ('Bajaj Discover 125', 50000, 2016, 'Individual', '1st owner', 42000)]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Preview the data
# MAGIC * Let us first preview the data.

# COMMAND ----------

attributes

# COMMAND ----------

type(attributes)

# COMMAND ----------

bike_details

# COMMAND ----------

type(bike_details)

# COMMAND ----------

bike_details[0]

# COMMAND ----------

type(bike_details[0])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Provide the solution
# MAGIC Now come up with the solution by developing the required logic. Once the logic is developed, go to the next step to take care of the validation.

# COMMAND ----------

# Your code should go here

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC Here are the steps to validate the function.

# COMMAND ----------

display(bike_details_df)

# COMMAND ----------

bike_details_df.columns # ['name', 'selling_price', 'year', 'seller_type', 'owner', 'km_driven']

# COMMAND ----------

bike_details_df.count() # 10

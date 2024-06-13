# Databricks notebook source
# MAGIC %md
# MAGIC ## Sort Data by Scheduled Dates
# MAGIC
# MAGIC Develop logic to sort the data by scheduled dates. We will be providing Spark Data Frame that contain Name, Country as well as Scheduled Date.
# MAGIC * Develop the logic which performs **composite sorting** on `aspirants_df` based on scheduled date and then name.
# MAGIC * Data should be sorted in ascending order by date and then in ascending order by name.

# COMMAND ----------

aspirants = [('Pardha Saradhi', 'India', '7/31/2021'),
 ('Asasri', 'India', '8/10/2021'),
 ('Sai Akshith', 'India', '7/30/2021'),
 ('Anmol', 'India', '7/5/2021'),
 ('Shravan', 'India', '7/28/2021'),
 ('Aditya', 'USA', '7/31/2021'),
 ('Prasanth ', 'USA', '8/14/2021'),
 ('Sahana', 'India', '7/26/2021'),
 ('Surendranatha Reddy', 'India', '7/25/2021'),
 ('Venkat ', 'USA', '7/26/2021')]

aspirants_df = spark.createDataFrame(aspirants, schema='name STRING, country STRING, scheduled_date STRING')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1: Preview the data
# MAGIC
# MAGIC Let us first preview the data.

# COMMAND ----------

aspirants_df

# COMMAND ----------

aspirants_df.count()

# COMMAND ----------

display(aspirants_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Provide the solution
# MAGIC
# MAGIC Now come up with the solution by developing the required logic. Once the function is developed, go to the next step to take care of the validation.

# COMMAND ----------

spark.sql("SELECT to_date('7/5/2021', 'd/M/yyyy')").show()

# COMMAND ----------

# The logic should go here
from pyspark.sql.functions import to_date, col
def sort_data_by_scheduled_date(aspirants_df):
    sorted_aspirants = aspirants_df. \
        orderBy(to_date('scheduled_date', 'M/d/yyyy').alias('scheduled_date'), col('name'))
    return sorted_aspirants

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells.
# MAGIC * Here is the expected output. Compare the results with this list of tuples.
# MAGIC
# MAGIC ```python
# MAGIC [('Anmol', 'India', '7/5/2021'),
# MAGIC  ('Surendranatha Reddy', 'India', '7/25/2021'),
# MAGIC  ('Sahana', 'India', '7/26/2021'),
# MAGIC  ('Venkat ', 'USA', '7/26/2021'),
# MAGIC  ('Shravan', 'India', '7/28/2021'),
# MAGIC  ('Sai Akshith', 'India', '7/30/2021'),
# MAGIC  ('Aditya', 'USA', '7/31/2021'),
# MAGIC  ('Pardha Saradhi', 'India', '7/31/2021'),
# MAGIC  ('Asasri', 'India', '8/10/2021'),
# MAGIC  ('Prasanth ', 'USA', '8/14/2021')]
# MAGIC ```

# COMMAND ----------

sorted_aspirants = sort_data_by_scheduled_date(aspirants_df)

# COMMAND ----------

display(sorted_aspirants) # Data should be sorted in ascending order by date and then by name

# COMMAND ----------

sorted_aspirants.count() # It should be 10

# COMMAND ----------



# Databricks notebook source
# MAGIC %md
# MAGIC ## Get all unique reasons
# MAGIC
# MAGIC Develop a function which gives list of unique reasons.
# MAGIC * We will provide the data in the form of list of dicts.
# MAGIC * Each element will have data related to multiple attributes associated with those who want to take the assessments.
# MAGIC * Develop a function which does the following.
# MAGIC   * It should take one argument - the list of aspirants.
# MAGIC   * You need to include the logic to find all the unique reasons. Each record might contain more than one reasons which are comma separated. You need process those with appropriate functions.
# MAGIC   * There should not be spaces before the reason or after the reason.
# MAGIC   * Return all the reasons as sorted list. The elements in the list should be sorted in alphanumeric order.
# MAGIC
# MAGIC **Restrictions: You should only use loops or first class functions such as map, filter etc.  Do not use Pandas.**

# COMMAND ----------

students = [{'Name': 'Pardha Saradhi',
  'Reason': 'To be part of ITVersity Professionals Database to work on paid part-time opportunities',
  'Current Status': 'Experienced Professionals (10+ years of experience)',
  'Python Rating': '3',
  'Scheduled Date': '7/31/2021',
  'Current Country': 'India'},
 {'Name': 'Asasri',
  'Reason': 'Self assess to understand where I stand in Python',
  'Current Status': 'Freshers or recent year pass outs looking for entry level jobs',
  'Python Rating': '2',
  'Scheduled Date': '8/10/2021',
  'Current Country': 'India'},
 {'Name': 'Sai Akshith',
  'Reason': 'Self assess to understand where I stand in Python, Technical Screening Preparation (tests as well as interviews), To be part of ITVersity Professionals Database to work on paid part-time opportunities',
  'Current Status': 'Entry level professional (less than 2 years of experience)',
  'Python Rating': '3',
  'Scheduled Date': '7/30/2021',
  'Current Country': 'India'},
 {'Name': 'Anmol',
  'Reason': 'Self assess to understand where I stand in Python, To be part of ITVersity Professionals Database to work on paid part-time opportunities',
  'Current Status': 'Experienced Professionals (2 to 5 years of experience)',
  'Python Rating': '2',
  'Scheduled Date': '7/25/2021',
  'Current Country': 'India'},
 {'Name': 'Shravan',
  'Reason': 'Self assess to understand where I stand in Python, Technical Screening Preparation (tests as well as interviews)',
  'Current Status': 'Experienced Professionals (2 to 5 years of experience)',
  'Python Rating': '1',
  'Scheduled Date': '7/28/2021',
  'Current Country': 'India'},
 {'Name': 'Aditya',
  'Reason': 'Self assess to understand where I stand in Python, Technical Screening Preparation (tests as well as interviews), Placement Assistance for full time opportunities, To be part of ITVersity Professionals Database to work on paid part-time opportunities',
  'Current Status': 'Experienced Professionals (5 to 10 years of experience)',
  'Python Rating': '1',
  'Scheduled Date': '7/31/2021',
  'Current Country': 'USA'},
 {'Name': 'Prasanth ',
  'Reason': 'Self assess to understand where I stand in Python',
  'Current Status': 'Experienced Professionals (10+ years of experience)',
  'Python Rating': '2',
  'Scheduled Date': '8/14/2021',
  'Current Country': 'USA'},
 {'Name': 'Sahana',
  'Reason': 'Self assess to understand where I stand in Python, Placement Assistance for full time opportunities',
  'Current Status': 'Entry level professional (less than 2 years of experience)',
  'Python Rating': '4',
  'Scheduled Date': '7/26/2021',
  'Current Country': 'India'}]

students_df = spark.createDataFrame(students)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1: Preview the data
# MAGIC
# MAGIC Let us first preview the data.

# COMMAND ----------

display(students_df)

# COMMAND ----------

students_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Provide the solution
# MAGIC
# MAGIC Now come up with the solution by developing the required logic. Once the function is developed, go to the next step to take care of the validation.

# COMMAND ----------

from pyspark.sql.functions import explode, split

def get_unique_reasons(students_df):
    unique_reasons = students_df. \
        select(explode(split('Reason', ', ')).alias('Reason')). \
        distinct()
    return unique_reasons

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells.
# MAGIC * Here is the expected output.
# MAGIC
# MAGIC ```python
# MAGIC [{'Reason': 'To be part of ITVersity Professionals Database to work on paid part-time opportunities'},
# MAGIC  {'Reason': 'Self assess to understand where I stand in Python'},
# MAGIC  {'Reason': 'Technical Screening Preparation (tests as well as interviews)'},
# MAGIC  {'Reason': 'Placement Assistance for full time opportunities'}]
# MAGIC ```

# COMMAND ----------

unique_reasons = get_unique_reasons(students_df)

# COMMAND ----------

display(unique_reasons)

# COMMAND ----------

unique_reasons.count() # 4

# COMMAND ----------

unique_reasons.toPandas().to_dict(orient='records')

# COMMAND ----------



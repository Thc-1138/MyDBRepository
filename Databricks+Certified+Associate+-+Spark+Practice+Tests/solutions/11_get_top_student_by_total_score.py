# Databricks notebook source
# MAGIC %md
# MAGIC ## Get Top Student by Total Score
# MAGIC
# MAGIC Develop a function to get the top student by total score. This is primarily to test the ability to manipulate Spark Data Frames, sort the data and get the top record.
# MAGIC * We will provide Spark Data Frame with student id followed by scores for different subjects.
# MAGIC * Develop a function which takes students as input and return the topper with highest total score.

# COMMAND ----------

students = [(1, 72, 72, 74), (2, 69, 90, 88), (3, 90, 95, 93), (4, 47, 47, 44), (5, 76, 78, 75), (6, 71, 83, 78)]

students_df = spark.createDataFrame(students, schema='student_id INT, math INT, social INT, science INT')

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
# MAGIC
# MAGIC **Hint: Sort the data by total score in descending order and use `first` to get the highest scoring student details.**

# COMMAND ----------

from pyspark.sql.functions import col
def get_topper_by_total_score(students_df):
    ## your code should go here
    topper_by_total_score = students_df. \
        withColumn('total_score', col('math') + col('social') + col('science')). \
        orderBy(col('total_score').desc()). \
        first()
    return topper_by_total_score

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells.
# MAGIC * The student id with highest total score is **3**.

# COMMAND ----------

topper_by_total_score = get_topper_by_total_score(students_df)

# COMMAND ----------

topper_by_total_score['student_id'] # 3

# COMMAND ----------

type(topper_by_total_score['student_id']) # int

# COMMAND ----------



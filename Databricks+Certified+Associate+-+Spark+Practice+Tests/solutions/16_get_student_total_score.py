# Databricks notebook source
# MAGIC %md
# MAGIC ## Get Student Total Score
# MAGIC
# MAGIC Develop a function to convert get the total score of each student. This is primarily to test the ability to manipulate dicts using first class functions such as map.
# MAGIC * We will provide list of dicts with student id and scores for different subjects.
# MAGIC * Develop a function which takes students as input and return students including individual total score.
# MAGIC * You need to add another element to each of the dicts with key `total_score`.
# MAGIC * The output should be sorted in descending order by total.
# MAGIC
# MAGIC ```{note}
# MAGIC Hint: You need to define and call named function as part of the map to add `total_score` to each of the dicts in the list.
# MAGIC ```
# MAGIC
# MAGIC **Restrictions: You should not use loops or Pandas to solve this problem. Use first class functions such as `map`.**

# COMMAND ----------

students = [
    {'student_id': 1, 'math_score': 72, 'reading_score': 72, 'writing_score': 74},
    {'student_id': 2, 'math_score': 69, 'reading_score': 90, 'writing_score': 88},
    {'student_id': 3, 'math_score': 90, 'reading_score': 95, 'writing_score': 93},
    {'student_id': 4, 'math_score': 47, 'reading_score': 47, 'writing_score': 44},
    {'student_id': 5, 'math_score': 76, 'reading_score': 78, 'writing_score': 75},
    {'student_id': 6, 'math_score': 71, 'reading_score': 83, 'writing_score': 78}
]

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

from pyspark.sql.functions import col

def get_students_with_total_scores(students_df):
    ## your code should go here
    ## Make sure to create another function to compute total and update the dict
    students_with_total_scores = students_df. \
        withColumn('total_score', col('math_score') + col('reading_score') + col('writing_score')). \
        orderBy(col('total_score').desc()). \
        select('student_id', 'math_score', 'reading_score', 'writing_score', 'total_score')
    return students_with_total_scores

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells.
# MAGIC * Here is the expected output.
# MAGIC
# MAGIC ```python
# MAGIC [{'student_id': 3,
# MAGIC   'math_score': 90,
# MAGIC   'reading_score': 95,
# MAGIC   'writing_score': 93,
# MAGIC   'total_score': 278},
# MAGIC  {'student_id': 2,
# MAGIC   'math_score': 69,
# MAGIC   'reading_score': 90,
# MAGIC   'writing_score': 88,
# MAGIC   'total_score': 247},
# MAGIC  {'student_id': 6,
# MAGIC   'math_score': 71,
# MAGIC   'reading_score': 83,
# MAGIC   'writing_score': 78,
# MAGIC   'total_score': 232},
# MAGIC  {'student_id': 5,
# MAGIC   'math_score': 76,
# MAGIC   'reading_score': 78,
# MAGIC   'writing_score': 75,
# MAGIC   'total_score': 229},
# MAGIC  {'student_id': 1,
# MAGIC   'math_score': 72,
# MAGIC   'reading_score': 72,
# MAGIC   'writing_score': 74,
# MAGIC   'total_score': 218},
# MAGIC  {'student_id': 4,
# MAGIC   'math_score': 47,
# MAGIC   'reading_score': 47,
# MAGIC   'writing_score': 44,
# MAGIC   'total_score': 138}]
# MAGIC ```

# COMMAND ----------

students_with_total_scores = get_students_with_total_scores(students_df)

# COMMAND ----------

display(students_with_total_scores) # 6

# COMMAND ----------

students_with_total_scores.count() # 6

# COMMAND ----------

students_with_total_scores.toPandas().to_dict(orient='records')

# COMMAND ----------



# Databricks notebook source
# MAGIC %md
# MAGIC ## Get unique programming languages
# MAGIC
# MAGIC Develop a function which takes a delimited string as input and returns unique values ignoring the case.
# MAGIC * We have a data frame with single column and single row. The only value in the Data Frame is nothing but a string of programming languages which are delimited by `,`.
# MAGIC * However the programming languages might be in mixed case. Also some of the programming languages have spaces in the beginning or the end.
# MAGIC * We need to ignore spaces and also ignore the case to get unique list of programming languages.
# MAGIC * Output should all be lower case, without leading or trailing spaces. The data type of the output should be `list`. Data should be sorted in ascending order.

# COMMAND ----------

programming_languages = [('Python, Java , java,python, Scala, java script, python, Go, scala,java, Ruby, go, ruby, Java Script', )]

# COMMAND ----------

df = spark.createDataFrame(programming_languages, schema='langs STRING')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1: Preview the data
# MAGIC * Let us first preview the data.

# COMMAND ----------

display(df)

# COMMAND ----------

type(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Provide the solution
# MAGIC Now come up with the solution by developing the required logic. Once the function is developed, go to the next step to take care of the validation.

# COMMAND ----------

def get_unique_programming_languages(programming_languages):
    # Your solution should go here
    return unique_programming_languages

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Here is the expected output.
# MAGIC
# MAGIC ```python
# MAGIC [{'lang': 'go'},
# MAGIC  {'lang': 'java'},
# MAGIC  {'lang': 'java script'},
# MAGIC  {'lang': 'python'},
# MAGIC  {'lang': 'ruby'},
# MAGIC  {'lang': 'scala'}]
# MAGIC ```

# COMMAND ----------

unique_programming_languages = get_unique_programming_languages(df)

# COMMAND ----------

display(unique_programming_languages)

# COMMAND ----------

unique_programming_languages.count() # 6

# COMMAND ----------

unique_programming_languages.toPandas().to_dict(orient='records')

# COMMAND ----------



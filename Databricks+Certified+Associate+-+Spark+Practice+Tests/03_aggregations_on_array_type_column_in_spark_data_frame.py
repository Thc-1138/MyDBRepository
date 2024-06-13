# Databricks notebook source
# MAGIC %md
# MAGIC ## Aggregations on Array Type Column in Spark Data Frame
# MAGIC
# MAGIC Develop a function to get number of times the color is repeated in arrays in the Data Frame. The logic should check whether the color exists or not.
# MAGIC * The input data is in the form of Spark Data Frame. Each column in the Data Frame is of type Array.
# MAGIC * Each Array contain multiple colors.
# MAGIC * The function should take 2 arguments. The first argument is Spark Data Frame which contain colors. The second argument is the color which you want to check.
# MAGIC * If the color that is passed as second argument, exists in any of the tuples, then the function should return number of times it is present across all the rows of Arrays.
# MAGIC * The characters in the second argument might be passed in any case. However, we need to perform case insensitive search.

# COMMAND ----------

colors = [
    (('Red', 'White', 'Yellow'),),
    (('YELLOW', 'Pink', 'red'),),
    (('blue', 'Yellow', 'Lime'),)
]

colors_df = spark.createDataFrame(colors, schema='colors ARRAY<STRING>')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Preview the data
# MAGIC * Let us first preview the data.

# COMMAND ----------

colors_df

# COMMAND ----------

colors_df.count()

# COMMAND ----------

colors_df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Provide the solution
# MAGIC Now come up with the solution by developing the required logic. Once the function is developed, go to the next step to take care of the validation.

# COMMAND ----------

def color_count(colors_df, color):
    # your code should go here
    return cnt

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC * Here is the expected output.

# COMMAND ----------

color_count(colors_df, 'Red') # 2

# COMMAND ----------

color_count(colors_df, 'red') # 2

# COMMAND ----------

color_count(colors_df, 'Black') # 0

# COMMAND ----------

color_count(colors_df, 'YELLOW') # 3

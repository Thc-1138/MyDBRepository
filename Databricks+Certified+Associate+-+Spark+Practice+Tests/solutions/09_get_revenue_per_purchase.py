# Databricks notebook source
# MAGIC %md
# MAGIC ## Get revenue per purchase
# MAGIC Develop a function which returns a new Spark Data Frame with new column holding revenue. 
# MAGIC * Following are the details about each item in the Data Frame.
# MAGIC   * It has 4 columns - order id, book title, quantity, retail prices of each book.
# MAGIC * We can compute the revenue of each purchase by multiplying quantity and the retail price of each book. Look at the expected output for further details.
# MAGIC * The function should take `purchases_df` as input and it should return a new Data Frame with order id, book title and the revenue. The revenue should be rounded off to 2 decimals.

# COMMAND ----------

purchases = [ 
    [34587, "Learning Python, Mark Lutz", 4, 40.95], 
    [98762, "Programming Python, Mark Lutz", 5, 56.80], 
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

purchases_df = spark.createDataFrame(purchases, 'order_id INT, book_title STRING, quantity INT, retail_price FLOAT')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Preview the data
# MAGIC * Let us first preview the data.

# COMMAND ----------

display(purchases_df)

# COMMAND ----------

purchases_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Provide the solution
# MAGIC Now come up with the solution by developing the required logic. Once the function is developed, go to the next step to take care of the validation.

# COMMAND ----------

from pyspark.sql.functions import col, round
def get_revenue_per_item(purchases_df):
    # your code should go here
    revenue_per_item = purchases_df. \
        withColumn('revenue', round(col('quantity') * col('retail_price'), 2)). \
        drop('quantity', 'retail_price')
    return revenue_per_item

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Here is the expected output. Ignore rounding off issue while converting to Python list to validate the output.
# MAGIC ```python
# MAGIC [{'order_id': 34587,
# MAGIC   'book_title': 'Learning Python, Mark Lutz',
# MAGIC   'revenue': 163.8000030517578},
# MAGIC  {'order_id': 98762,
# MAGIC   'book_title': 'Programming Python, Mark Lutz',
# MAGIC   'revenue': 284.0},
# MAGIC  {'order_id': 77226,
# MAGIC   'book_title': 'Head First Python, Paul Barry',
# MAGIC   'revenue': 98.8499984741211},
# MAGIC  {'order_id': 88112,
# MAGIC   'book_title': 'Einführung in Python3, Bernd Klein',
# MAGIC   'revenue': 74.97000122070312}]
# MAGIC ```

# COMMAND ----------

items = get_revenue_per_item(purchases_df)

# COMMAND ----------

display(items) # There should be 4 records with 3 columns. Revenue should be rounded off to 2 decimals.

# COMMAND ----------

items.toPandas().to_dict(orient='records')

# COMMAND ----------



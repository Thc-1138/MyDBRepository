# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# DBTITLE 0,--i18n-f71eff64-cf6e-469a-ab37-a297936c4980
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC # Active Users Lab
# MAGIC Plot daily active users and average active users by day of week.
# MAGIC 1. Extract timestamp and date of events
# MAGIC 2. Get daily active users
# MAGIC 3. Get average number of active users by day of week
# MAGIC 4. Sort day of week in correct order

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-3a6a78da-1772-441e-b73a-eff2e82561bb
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Setup
# MAGIC Run the cell below to create the starting DataFrame of user IDs and timestamps of events logged on the BedBricks website.

# COMMAND ----------

from pyspark.sql.functions import col

df = (spark
      .read
      .format("delta")
      .load(DA.paths.events)
      .select("user_id", col("event_timestamp").alias("ts"))
     )

display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-7fa26321-781b-4633-bce4-5b86082adbcc
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### 1. Extract timestamp and date of events
# MAGIC - Convert **`ts`** from microseconds to seconds by dividing by 1 million and cast to timestamp
# MAGIC - Add **`date`** column by converting **`ts`** to date

# COMMAND ----------

# TODO
datetime_df = (df.withColumn("ts", (col("ts")/1e6).cast("timestamp"))
               .withColumn("date", col("ts").cast("date"))
)
display(datetime_df)

# COMMAND ----------

# DBTITLE 0,--i18n-50e248b0-9067-4ec0-b633-1862739315f1
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC
# MAGIC **1.1: CHECK YOUR WORK**

# COMMAND ----------

from pyspark.sql.types import DateType, StringType, StructField, StructType, TimestampType

expected1a = StructType([StructField("user_id", StringType(), True),
                         StructField("ts", TimestampType(), True),
                         StructField("date", DateType(), True)])

result1a = datetime_df.schema

assert expected1a == result1a, "datetime_df does not have the expected schema"
print("All test pass")

# COMMAND ----------

import datetime

expected1b = datetime.date(2020, 6, 19)
result1b = datetime_df.sort("date").first().date

assert expected1b == result1b, "datetime_df does not have the expected date values"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-cffda679-267e-4934-9316-f33d68f1fff6
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### 2. Get daily active users
# MAGIC - Group by date
# MAGIC - Aggregate approximate count of distinct **`user_id`** and alias to "active_users"
# MAGIC   - Recall built-in function to get **approximate count distinct** (also recall:  approximate count distinct is different than count distinct!)
# MAGIC - Sort by date
# MAGIC - Plot as line graph

# COMMAND ----------

from pyspark.sql.functions import approx_count_distinct
active_users_df = (datetime_df.groupBy("date").agg(approx_count_distinct("user_id").alias("active_users")).sort("date")
)
display(active_users_df)

# COMMAND ----------

# DBTITLE 0,--i18n-168eed92-68bf-4966-98b6-f92bc44fbe67
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC
# MAGIC **2.1: CHECK YOUR WORK**

# COMMAND ----------

from pyspark.sql.types import LongType

expected2a = StructType([StructField("date", DateType(), True),
                         StructField("active_users", LongType(), False)])

result2a = active_users_df.schema

assert expected2a == result2a, "active_users_df does not have the expected schema"
print("All test pass")

# COMMAND ----------

expected2b = [(datetime.date(2020, 6, 19), 251573), (datetime.date(2020, 6, 20), 357215), (datetime.date(2020, 6, 21), 305055), (datetime.date(2020, 6, 22), 239094), (datetime.date(2020, 6, 23), 243117)]

result2b = [(row.date, row.active_users) for row in active_users_df.orderBy("date").take(5)]

assert expected2b == result2b, "active_users_df does not have the expected values"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-ac71e88e-aa3d-4032-8741-876f0d8ff8da
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### 3. Get average number of active users by day of week
# MAGIC - Add **`day`** column by extracting day of week from **`date`** using a datetime pattern string - the expected output here will be a day name, not a number (e.g. **`Mon`**, not **`1`**)
# MAGIC - Group by **`day`**
# MAGIC - Aggregate average of **`active_users`** and alias to "avg_users"

# COMMAND ----------

from pyspark.sql.functions import date_format, avg

active_dow_df = (active_users_df.withColumn("day", date_format("date", "E")).groupBy("day").agg(avg("active_users").alias("avg_users"))
)
display(active_dow_df)

# COMMAND ----------

# DBTITLE 0,--i18n-889c1b5c-f870-45d0-8cc0-5e1c58f6640e
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC
# MAGIC **3.1: CHECK YOUR WORK**

# COMMAND ----------

from pyspark.sql.types import DoubleType

expected3a = StructType([StructField("day", StringType(), True),
                         StructField("avg_users", DoubleType(), True)])

result3a = active_dow_df.schema

assert expected3a == result3a, "active_dow_df does not have the expected schema"
print("All test pass")

# COMMAND ----------

expected3b = [("Fri", 247180.66666666666), ("Mon", 238195.5), ("Sat", 278482.0), ("Sun", 282905.5), ("Thu", 264620.0), ("Tue", 260942.5), ("Wed", 227214.0)]

result3b = [(row.day, row.avg_users) for row in active_dow_df.sort("day").collect()]

assert expected3b == result3b, "active_dow_df does not have the expected values"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-f4b41974-87d7-47fe-81f8-93fd5c99fbe1
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Clean up classroom

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>

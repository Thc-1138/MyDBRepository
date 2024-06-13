# Databricks notebook source
# MAGIC %md
# MAGIC ## Get number of companies per sector
# MAGIC
# MAGIC Develop the function to get the number of companies per sector. As part of this Spark Practice Test, we are primarily evaluating the ability to group the data in Spark Data Frame by a key and perform aggregations.
# MAGIC * The input Data Frame contains the name of company and it's sector.
# MAGIC * The output Data Frame should contain sector as key and number of companies per sector as it's values. 
# MAGIC * The output Data Frame should be sorted in ascending order by sector name.
# MAGIC * Also the second column in the output data frame should be **company_count**.

# COMMAND ----------

companies=[
    ('Accenture', 'IT'),
    ('Apple', 'IT'),
    ('Adobe Systems Inc', 'IT'),
    ('Alphabet', 'IT'),
    ('Bank of America Corp', 'Financials'),
    ('Biogen Inc', 'Health Care'),
    ('Campbell Soup', 'Consumer Staples'),
    ('Dr Pepper Snapple Group', 'Consumer Staples'),
    ('ebay Inc', 'IT'),
    ('FedEx Corporation', 'Industrials'),
    ('Ford Motors', 'Consumer Products'),
    ('General Motors', 'Consumer Products'),
    ('Harley-Davidson', 'Consumer Products'),
    ('Hewlett Packard Enterprise', 'IT'),
    ('Intel Corp', 'IT'),
    ('JP Morgan', 'Financials'),
    ('Johnson & Johnson', 'Health Care'),
    ('Microsft Corp', 'IT'),
    ('Netflix Inc', 'IT'),
    ('Nike', 'Consumer Products')
]

companies_df = spark.createDataFrame(companies, schema='company_name STRING, sector STRING')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1: Preview the data
# MAGIC
# MAGIC Let us first preview the data.

# COMMAND ----------

display(companies_df)

# COMMAND ----------

companies_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Provide the solution
# MAGIC
# MAGIC Now come up with the solution by developing the required logic. Once the function is developed, go to the next step to take care of the validation.

# COMMAND ----------

def get_company_count_per_sector(companies_df):
    # Develop your logic here
    return company_count_per_sector

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells.
# MAGIC * Here is the expected output.
# MAGIC
# MAGIC ```python
# MAGIC [{'sector': 'Consumer Products', 'company_count': 4},
# MAGIC  {'sector': 'Consumer Staples', 'company_count': 2},
# MAGIC  {'sector': 'Financials', 'company_count': 2},
# MAGIC  {'sector': 'Health Care', 'company_count': 2},
# MAGIC  {'sector': 'IT', 'company_count': 9},
# MAGIC  {'sector': 'Industrials', 'company_count': 1}]
# MAGIC ```

# COMMAND ----------

company_count_per_sector = get_company_count_per_sector(companies_df)

# COMMAND ----------

display(company_count_per_sector)

# COMMAND ----------

company_count_per_sector.count() # 6

# COMMAND ----------

company_count_per_sector.toPandas().to_dict(orient='records')

# COMMAND ----------



# Databricks notebook source
# MAGIC %md
# MAGIC ## Get list of companies per sector
# MAGIC
# MAGIC Develop the function to get the company from each sector from the dictionary containing name and it's corresponding sector.
# MAGIC * This scanerio can be solved by the help of conventional loops or itertools.
# MAGIC * The input dictionary contains the name of company and it's sector.
# MAGIC * The output dictionary should contain sector as key and companies per sector as it's values. The company     names should as part of a list with sector as key.

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

from pyspark.sql.functions import collect_list, size

def get_companies_per_sector(companies_df):
    # Develop your logic here
    companies_per_sector = companies_df. \
        groupBy('sector'). \
        agg(collect_list('company_name').alias('company_names')). \
        orderBy(size('company_names').desc())
    return companies_per_sector

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells.
# MAGIC * Here is the expected output.
# MAGIC
# MAGIC ```
# MAGIC [{'sector': 'IT',
# MAGIC   'company_names': array(['Accenture', 'Apple', 'Adobe Systems Inc', 'Alphabet', 'ebay Inc',
# MAGIC          'Hewlett Packard Enterprise', 'Intel Corp', 'Microsft Corp',
# MAGIC          'Netflix Inc'], dtype=object)},
# MAGIC  {'sector': 'Consumer Products',
# MAGIC   'company_names': array(['Ford Motors', 'General Motors', 'Harley-Davidson', 'Nike'],
# MAGIC         dtype=object)},
# MAGIC  {'sector': 'Financials',
# MAGIC   'company_names': array(['Bank of America Corp', 'JP Morgan'], dtype=object)},
# MAGIC  {'sector': 'Health Care',
# MAGIC   'company_names': array(['Biogen Inc', 'Johnson & Johnson'], dtype=object)},
# MAGIC  {'sector': 'Consumer Staples',
# MAGIC   'company_names': array(['Campbell Soup', 'Dr Pepper Snapple Group'], dtype=object)},
# MAGIC  {'sector': 'Industrials',
# MAGIC   'company_names': array(['FedEx Corporation'], dtype=object)}]
# MAGIC ```

# COMMAND ----------

display(get_companies_per_sector(companies_df))

# COMMAND ----------

get_companies_per_sector(companies_df).toPandas().to_dict(orient='records')

# COMMAND ----------



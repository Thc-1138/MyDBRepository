# Databricks notebook source
# MAGIC %md
# MAGIC ## Filter companies by sector and Dividend
# MAGIC
# MAGIC Develop the function which returns companies related to the sector which pay Dividend of greater than or equal to specified value.
# MAGIC * Output Data Frame should contain data based on the criteria.
# MAGIC * Output Data Frame should be sorted in descending order by dividend.

# COMMAND ----------

companies = [{'Name': 'Accenture',
  'Sector': 'IT',
  'Price': 222.89,
  'Dividend': 2.33,
  'EarningsPerShare': 7.92},
 {'Name': 'Apple',
  'Sector': 'IT',
  'Price': 155.15,
  'Dividend': 1.57,
  'EarningsPerShare': 9.2},
 {'Name': 'Adobe Systems Inc',
  'Sector': 'IT',
  'Price': 185.16,
  'Dividend': 0.0,
  'EarningsPerShare': 3.39},
 {'Name': 'Alphabet',
  'Sector': 'IT',
  'Price': 1007.71,
  'Dividend': 0.0,
  'EarningsPerShare': 22.27},
 {'Name': 'Bank of America Corp',
  'Sector': 'Finacials',
  'Price': 29.74,
  'Dividend': 1.53,
  'EarningsPerShare': 1.55},
 {'Name': 'Biogen Inc',
  'Sector': 'Health Care',
  'Price': 311.79,
  'Dividend': 0.0,
  'EarningsPerShare': 11.94},
 {'Name': 'Campbell Soup',
  'Sector': 'Consumer Staples',
  'Price': 44.83,
  'Dividend': 3.12,
  'EarningsPerShare': 2.89},
 {'Name': 'Dr Pepper Snapple Group',
  'Sector': 'Consumer Staples',
  'Price': 116.93,
  'Dividend': 1.96,
  'EarningsPerShare': 4.54},
 {'Name': 'ebay Inc',
  'Sector': 'IT',
  'Price': 41.02,
  'Dividend': 0.0,
  'EarningsPerShare': -1.07},
 {'Name': 'FedEx Corporation',
  'Sector': 'Industrials',
  'Price': 239.27,
  'Dividend': 0.79,
  'EarningsPerShare': 11.07},
 {'Name': 'Ford Motors',
  'Sector': 'Consumer Products',
  'Price': 10.43,
  'Dividend': 6.78,
  'EarningsPerShare': 1.9},
 {'Name': 'General Motors',
  'Sector': 'Consumer Products',
  'Price': 40.75,
  'Dividend': 3.58,
  'EarningsPerShare': 6.0},
 {'Name': 'Harley-Davidson',
  'Sector': 'Consumer Products',
  'Price': 47.54,
  'Dividend': 3.02,
  'EarningsPerShare': 2.98},
 {'Name': 'Hewlett Packard Enterprise',
  'Sector': 'IT',
  'Price': 15.04,
  'Dividend': 1.92,
  'EarningsPerShare': 0.21},
 {'Name': 'Intel Corp',
  'Sector': 'IT',
  'Price': 42.75,
  'Dividend': 2.65,
  'EarningsPerShare': 1.98},
 {'Name': 'JP Morgan',
  'Sector': 'Finacials',
  'Price': 107.88,
  'Dividend': 1.98,
  'EarningsPerShare': 6.3},
 {'Name': 'Johnson & Johnson',
  'Sector': 'IT',
  'Price': 126.36,
  'Dividend': 2.55,
  'EarningsPerShare': 0.39},
 {'Name': 'Microsoft Corp',
  'Sector': 'IT',
  'Price': 85.01,
  'Dividend': 1.87,
  'EarningsPerShare': 2.97},
 {'Name': 'Netflix Inc',
  'Sector': 'IT',
  'Price': 250.01,
  'Dividend': 0.0,
  'EarningsPerShare': 1.25},
 {'Name': 'Nike',
  'Sector': 'Consumer Products',
  'Price': 62.49,
  'Dividend': 1.21,
  'EarningsPerShare': 2.51}]

companies_df = spark.createDataFrame(companies)

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

from pyspark.sql.functions import col

def get_companies_by_sector_and_dividend(companies_df, sector, dividend):
    #Your code should go here
    companies_by_sector = companies_df. \
        filter((col('Sector') == sector) & (col('Dividend') >= 1.50)). \
        orderBy(col('Dividend').desc())
    return companies_by_sector

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells. Here is the desired output.
# MAGIC
# MAGIC ```
# MAGIC [{'Dividend': 2.65,
# MAGIC   'EarningsPerShare': 1.98,
# MAGIC   'Name': 'Intel Corp',
# MAGIC   'Price': 42.75,
# MAGIC   'Sector': 'IT'},
# MAGIC  {'Dividend': 2.55,
# MAGIC   'EarningsPerShare': 0.39,
# MAGIC   'Name': 'Johnson & Johnson',
# MAGIC   'Price': 126.36,
# MAGIC   'Sector': 'IT'},
# MAGIC  {'Dividend': 2.33,
# MAGIC   'EarningsPerShare': 7.92,
# MAGIC   'Name': 'Accenture',
# MAGIC   'Price': 222.89,
# MAGIC   'Sector': 'IT'},
# MAGIC  {'Dividend': 1.92,
# MAGIC   'EarningsPerShare': 0.21,
# MAGIC   'Name': 'Hewlett Packard Enterprise',
# MAGIC   'Price': 15.04,
# MAGIC   'Sector': 'IT'},
# MAGIC  {'Dividend': 1.87,
# MAGIC   'EarningsPerShare': 2.97,
# MAGIC   'Name': 'Microsoft Corp',
# MAGIC   'Price': 85.01,
# MAGIC   'Sector': 'IT'},
# MAGIC  {'Dividend': 1.57,
# MAGIC   'EarningsPerShare': 9.2,
# MAGIC   'Name': 'Apple',
# MAGIC   'Price': 155.15,
# MAGIC   'Sector': 'IT'}]
# MAGIC ```

# COMMAND ----------

companies_by_sector_and_dividend = get_companies_by_sector_and_dividend(companies_df, 'IT', 1.5)

# COMMAND ----------

display(companies_by_sector_and_dividend)

# COMMAND ----------

companies_by_sector_and_dividend.count() # 6

# COMMAND ----------

companies_by_sector_and_dividend.toPandas().to_dict(orient='records')

# COMMAND ----------

# MAGIC %md
# MAGIC You can check by entering another sector name and you should get the desired output related to that.

# COMMAND ----------



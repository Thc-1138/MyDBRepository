# Databricks notebook source
# MAGIC %md
# MAGIC ## Get count of companies by dividend status
# MAGIC
# MAGIC Develop function which get number of dividend paying and non paying companies using Spark Data Frame APIs.
# MAGIC * The input Data Frame contains the name of company, it's sector and other attributes.
# MAGIC * Develop a function which takes companies Data Frame as input and return 2 records. The output Data Frame should contain 2 columns and 2 rows.
# MAGIC * Column names are **Company Status** and **Company Count**.
# MAGIC * As part of **Non Dividend Paying**, we need to have count of companies with Dividend as 0.
# MAGIC * As part of **Dividend Paying**, we need to have count of companies with Divdend greater than 0.

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

def get_companies_by_dividend_payout(companies_df):
    # Your code should go here
    return companies_by_dividend_payout

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells.
# MAGIC * Here is the expected output.
# MAGIC
# MAGIC ```
# MAGIC [{'Company Status': 'Non Dividend Paying', 'Company Count': 5},
# MAGIC  {'Company Status': 'Dividend Paying', 'Company Count': 15}]
# MAGIC ```

# COMMAND ----------

companies_by_dividend_payout = get_companies_by_dividend_payout(companies_df)

# COMMAND ----------

display(companies_by_dividend_payout)

# COMMAND ----------

companies_by_dividend_payout.count() # 2

# COMMAND ----------

companies_by_dividend_payout.toPandas().to_dict(orient='records')

# COMMAND ----------



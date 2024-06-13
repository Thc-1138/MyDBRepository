# Databricks notebook source
# MAGIC %md
# MAGIC ## Apply Schema to Companies Data
# MAGIC
# MAGIC Develop a function which applies schema on top of data. The function shall take 2 arguments - data and attributes.
# MAGIC * Data should be passed in the form list of comma separated strings.
# MAGIC * Attributes should be passed in the form of a comma separated string.
# MAGIC * The function should return list of dicts. Refer to desired output.
# MAGIC * Make sure the numeric types in the dict are of type float.
# MAGIC
# MAGIC **Hint: This scanerio is to be solved by using zip() function**

# COMMAND ----------

fields = 'Name,Sector,Price,Dividend,EarningsPerShare'
# Name and Sector are of type strings
# Price, Dividend and EarningsPerShare are of typd Float or Double
# Using Fields above and data types build StructType

# COMMAND ----------

companies = [
    ('Accenture', 'IT', 222.89, 2.33, 7.92),
    ('Apple', 'IT', 155.15, 1.57, 9.2),
    ('Adobe Systems Inc', 'IT', 185.16, 0.0, 3.39),
    ('Alphabet', 'IT', 1007.71, 0.0, 22.27),
    ('ebay Inc', 'IT', 41.02, 0.0, -1.07),
    ('Hewlett Packard Enterprise', 'IT', 15.04, 1.92, 0.21),
    ('Intel Corp', 'IT', 42.75, 2.65, 1.98),
    ('Microsoft Corp', 'IT', 85.01, 1.87, 2.97),
    ('Netflix Inc', 'IT', 250.01, 0.0, 1.25)
]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1: Preview the Data
# MAGIC Let us preview the data.

# COMMAND ----------

companies

# COMMAND ----------

type(companies)

# COMMAND ----------

companies[0]

# COMMAND ----------

type(companies[0])

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Provide the Solution
# MAGIC Provide the solution below.

# COMMAND ----------

# Create Data Frame by applying schema using StructType

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC Let us validate the function by running the below cells.
# MAGIC
# MAGIC Here is the desired output
# MAGIC ```python
# MAGIC [{'Name': 'Accenture',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 222.89,
# MAGIC   'Dividend': 2.33,
# MAGIC   'EarningsPerShare': 7.92},
# MAGIC  {'Name': 'Apple',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 155.15,
# MAGIC   'Dividend': 1.57,
# MAGIC   'EarningsPerShare': 9.2},
# MAGIC  {'Name': 'Adobe Systems Inc',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 185.16,
# MAGIC   'Dividend': 0.0,
# MAGIC   'EarningsPerShare': 3.39},
# MAGIC  {'Name': 'Alphabet',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 1007.71,
# MAGIC   'Dividend': 0.0,
# MAGIC   'EarningsPerShare': 22.27},
# MAGIC  {'Name': 'ebay Inc',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 41.02,
# MAGIC   'Dividend': 0.0,
# MAGIC   'EarningsPerShare': -1.07},
# MAGIC  {'Name': 'Hewlett Packard Enterprise',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 15.04,
# MAGIC   'Dividend': 1.92,
# MAGIC   'EarningsPerShare': 0.21},
# MAGIC  {'Name': 'Intel Corp',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 42.75,
# MAGIC   'Dividend': 2.65,
# MAGIC   'EarningsPerShare': 1.98},
# MAGIC  {'Name': 'Microsoft Corp',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 85.01,
# MAGIC   'Dividend': 1.87,
# MAGIC   'EarningsPerShare': 2.97},
# MAGIC  {'Name': 'Netflix Inc',
# MAGIC   'Sector': 'IT',
# MAGIC   'Price': 250.01,
# MAGIC   'Dividend': 0.0,
# MAGIC   'EarningsPerShare': 1.25}]
# MAGIC ```

# COMMAND ----------

display(companies_with_attrs)

# COMMAND ----------

companies_with_attrs.count() # 9

# COMMAND ----------

companies_with_attrs.printSchema()

# COMMAND ----------

""" # Here is the desired output
[('Name', 'string'),
 ('Sector', 'string'),
 ('Price', 'double'),
 ('Dividend', 'double'),
 ('EarningsPerShare', 'double')]
"""

companies_with_attrs.dtypes

# COMMAND ----------

# Solution with schema as string

companies_schema = '''
    Name STRING,
    Sector STRING,
    Price DOUBLE,
    Dividend DOUBLE,
    EarningsPerShare DOUBLE
'''

companies_with_attrs = spark.createDataFrame(companies, schema=companies_schema)

display(companies_with_attrs)

# COMMAND ----------



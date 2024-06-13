# Databricks notebook source
# MAGIC %md
# MAGIC ## Sort Courses by Level and Enrollments
# MAGIC
# MAGIC Develop logic to sort the courses by suitability and number of enrollments. As part of this Spark Practice Test, we are primarily evaluating the ability to understand the composite sorting based on more than one field in the Spark Data Frame.
# MAGIC * We will provide course data in the form of a Data Frames - `courses_df`.
# MAGIC * Develop a function which takes the `courses_df` as input and sort the data by number of enrollments. The Data Frame contains 6 columns.
# MAGIC * Make sure the data is sorted in ascending order by level and then in numerically in descending order by number of enrollments.
# MAGIC * Here is the data provided below in the form of Spark Data Frame.

# COMMAND ----------

courses = ['1,2020 Complete Python Bootcamp: From Zero to Hero in Python,Beginner,1100093,4.6,318066',
 '4,Angular - The Complete Guide (2020 Edition),Intermediate,422557,4.6,129984',
 '12,Automate the Boring Stuff with Python Programming,Advanced,692617,4.6,70508',
 '10,Complete C# Unity Game Developer 2D,Advanced,364934,4.6,78989',
 '5,Java Programming Masterclass for Software Developers,Advanced,502572,4.6,123798',
 '15,Learn Python Programming Masterclass,Advanced,240790,4.5,58677',
 '3,Machine Learning A-Z™: Hands-On Python & R In Data Science,Intermediate,692812,4.5,132228',
 '14,Modern React with Redux [2020 Update],Intermediate,203214,4.7,60835',
 '8,Python for Data Science and Machine Learning Bootcamp,Intermediate,387789,4.6,87403',
 '6,"React - The Complete Guide (incl Hooks, React Router, Redux)",Intermediate,304670,4.6,90964',
 '18,Selenium WebDriver with Java -Basics to Advanced+Frameworks,Advanced,148562,4.6,49947',
 '21,Spring & Hibernate for Beginners (includes Spring Boot),Advanced,177053,4.6,45329',
 '7,The Complete 2020 Web Development Bootcamp,Beginner,270656,4.7,88098',
 '9,The Complete JavaScript Course 2020: Build Real Projects!,Intermediate,347979,4.6,83521',
 '16,The Complete Node.js Developer Course (3rd Edition),Advanced,202922,4.7,50885',
 '13,The Complete Web Developer Course 2.0,Intermediate,273598,4.5,63175',
 '11,The Data Science Course 2020: Complete Data Science Bootcamp,Beginner,325047,4.5,76907',
 '20,The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert,Beginner,203366,4.6,45382',
 '2,The Web Developer Bootcamp,Beginner,596726,4.6,182997',
 '19,Unreal Engine C++ Developer: Learn C++ and Make Video Games,Advanced,229005,4.5,45860',
 '17,iOS 13 & Swift 5 - The Complete iOS App Development Bootcamp,Advanced,179598,4.8,49972']

import pandas as pd

from io import StringIO
courses_pdf = pd.read_csv(
    StringIO("\n".join(courses)), 
    names=['course_id', 'course_name', 'level', 'enrolments', 'cumulative_rating', 'number_of_ratings']
)

courses_df = spark.createDataFrame(courses_pdf)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1: Preview the data
# MAGIC
# MAGIC Let us first preview the data.

# COMMAND ----------

display(courses_df)

# COMMAND ----------

courses_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Provide the solution
# MAGIC
# MAGIC Now come up with the solution by developing the required logic. Once the function is developed, go to the next step to take care of the validation.

# COMMAND ----------

# The logic should go here
from pyspark.sql.functions import col

def sort_courses_by_level_and_enrollments(courses_df):
    courses_sorted = courses_df. \
        orderBy('level', col('enrolments').desc())
    return courses_sorted

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Validate the function
# MAGIC
# MAGIC Let us validate the function by running below cells.
# MAGIC * Here is the expected output.
# MAGIC
# MAGIC ```python
# MAGIC [{'course_id': 12,
# MAGIC   'course_name': 'Automate the Boring Stuff with Python Programming',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 692617,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 70508},
# MAGIC  {'course_id': 5,
# MAGIC   'course_name': 'Java Programming Masterclass for Software Developers',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 502572,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 123798},
# MAGIC  {'course_id': 10,
# MAGIC   'course_name': 'Complete C# Unity Game Developer 2D',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 364934,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 78989},
# MAGIC  {'course_id': 15,
# MAGIC   'course_name': 'Learn Python Programming Masterclass',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 240790,
# MAGIC   'cumulative_rating': 4.5,
# MAGIC   'number_of_ratings': 58677},
# MAGIC  {'course_id': 19,
# MAGIC   'course_name': 'Unreal Engine C++ Developer: Learn C++ and Make Video Games',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 229005,
# MAGIC   'cumulative_rating': 4.5,
# MAGIC   'number_of_ratings': 45860},
# MAGIC  {'course_id': 16,
# MAGIC   'course_name': 'The Complete Node.js Developer Course (3rd Edition)',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 202922,
# MAGIC   'cumulative_rating': 4.7,
# MAGIC   'number_of_ratings': 50885},
# MAGIC  {'course_id': 17,
# MAGIC   'course_name': 'iOS 13 & Swift 5 - The Complete iOS App Development Bootcamp',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 179598,
# MAGIC   'cumulative_rating': 4.8,
# MAGIC   'number_of_ratings': 49972},
# MAGIC  {'course_id': 21,
# MAGIC   'course_name': 'Spring & Hibernate for Beginners (includes Spring Boot)',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 177053,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 45329},
# MAGIC  {'course_id': 18,
# MAGIC   'course_name': 'Selenium WebDriver with Java -Basics to Advanced+Frameworks',
# MAGIC   'level': 'Advanced',
# MAGIC   'enrolments': 148562,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 49947},
# MAGIC  {'course_id': 1,
# MAGIC   'course_name': '2020 Complete Python Bootcamp: From Zero to Hero in Python',
# MAGIC   'level': 'Beginner',
# MAGIC   'enrolments': 1100093,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 318066},
# MAGIC  {'course_id': 2,
# MAGIC   'course_name': 'The Web Developer Bootcamp',
# MAGIC   'level': 'Beginner',
# MAGIC   'enrolments': 596726,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 182997},
# MAGIC  {'course_id': 11,
# MAGIC   'course_name': 'The Data Science Course 2020: Complete Data Science Bootcamp',
# MAGIC   'level': 'Beginner',
# MAGIC   'enrolments': 325047,
# MAGIC   'cumulative_rating': 4.5,
# MAGIC   'number_of_ratings': 76907},
# MAGIC  {'course_id': 7,
# MAGIC   'course_name': 'The Complete 2020 Web Development Bootcamp',
# MAGIC   'level': 'Beginner',
# MAGIC   'enrolments': 270656,
# MAGIC   'cumulative_rating': 4.7,
# MAGIC   'number_of_ratings': 88098},
# MAGIC  {'course_id': 20,
# MAGIC   'course_name': 'The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert',
# MAGIC   'level': 'Beginner',
# MAGIC   'enrolments': 203366,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 45382},
# MAGIC  {'course_id': 3,
# MAGIC   'course_name': 'Machine Learning A-Z™: Hands-On Python & R In Data Science',
# MAGIC   'level': 'Intermediate',
# MAGIC   'enrolments': 692812,
# MAGIC   'cumulative_rating': 4.5,
# MAGIC   'number_of_ratings': 132228},
# MAGIC  {'course_id': 4,
# MAGIC   'course_name': 'Angular - The Complete Guide (2020 Edition)',
# MAGIC   'level': 'Intermediate',
# MAGIC   'enrolments': 422557,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 129984},
# MAGIC  {'course_id': 8,
# MAGIC   'course_name': 'Python for Data Science and Machine Learning Bootcamp',
# MAGIC   'level': 'Intermediate',
# MAGIC   'enrolments': 387789,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 87403},
# MAGIC  {'course_id': 9,
# MAGIC   'course_name': 'The Complete JavaScript Course 2020: Build Real Projects!',
# MAGIC   'level': 'Intermediate',
# MAGIC   'enrolments': 347979,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 83521},
# MAGIC  {'course_id': 6,
# MAGIC   'course_name': 'React - The Complete Guide (incl Hooks, React Router, Redux)',
# MAGIC   'level': 'Intermediate',
# MAGIC   'enrolments': 304670,
# MAGIC   'cumulative_rating': 4.6,
# MAGIC   'number_of_ratings': 90964},
# MAGIC  {'course_id': 13,
# MAGIC   'course_name': 'The Complete Web Developer Course 2.0',
# MAGIC   'level': 'Intermediate',
# MAGIC   'enrolments': 273598,
# MAGIC   'cumulative_rating': 4.5,
# MAGIC   'number_of_ratings': 63175},
# MAGIC  {'course_id': 14,
# MAGIC   'course_name': 'Modern React with Redux [2020 Update]',
# MAGIC   'level': 'Intermediate',
# MAGIC   'enrolments': 203214,
# MAGIC   'cumulative_rating': 4.7,
# MAGIC   'number_of_ratings': 60835}]
# MAGIC ```

# COMMAND ----------

courses_sorted = sort_courses_by_level_and_enrollments(courses_df)

# COMMAND ----------

display(courses_sorted)

# COMMAND ----------

courses_sorted.count() # 21

# COMMAND ----------

courses_sorted.toPandas().to_dict(orient='records')

# COMMAND ----------



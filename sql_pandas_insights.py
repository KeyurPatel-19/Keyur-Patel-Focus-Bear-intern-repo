import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# Load environment variables
load_dotenv()

# Read database credentials
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Create SQLAlchemy engine
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("Connected to PostgreSQL successfully!")


import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("Connected to PostgreSQL successfully!")

# Query 1
query_all_users = """
SELECT *
FROM users;
"""
df_users = pd.read_sql(query_all_users, engine)
print("\nAll Users:")
print(df_users)

# Query 2
query_active_users = """
SELECT name, email, country, subscription_type
FROM users
WHERE active = true;
"""
df_active = pd.read_sql(query_active_users, engine)
print("\nActive Users:")
print(df_active)

# Query 3
query_country_count = """
SELECT country, COUNT(*) AS total_users
FROM users
GROUP BY country
ORDER BY total_users DESC;
"""
df_country = pd.read_sql(query_country_count, engine)
print("\nUsers by Country:")
print(df_country)

# Query 4
query_avg_age = """
SELECT subscription_type, AVG(age) AS average_age
FROM users
GROUP BY subscription_type;
"""
df_avg_age = pd.read_sql(query_avg_age, engine)
print("\nAverage Age by Subscription:")
print(df_avg_age)


## Perform deeper data analysis in Pandas

print("----Deeper Analysys-----")

print("\nData Types:")
print(df_users.dtypes)

print("\nSummary Statistics:")
print(df_users.describe())

print("\nMissing Values:")
print(df_users.isnull().sum())

# Example 1: Filter premium users
print("Example 1: Filter premium users")

premium_users = df_users[df_users["subscription_type"] == "Premium"]
print("\nPremium Users:")
print(premium_users)

# Example 2: Find users older than 25
print("Example 2: Find users older than 25")

older_users = df_users[df_users["age"] > 25]
print("\nUsers older than 25:")
print(older_users[["name", "age", "country"]])

# Example 3: Group by country in Pandas
print("Example 3: Group by country in Pandas")

country_summary = df_users.groupby("country").agg(
    total_users=("id", "count"),
    average_age=("age", "mean")
).reset_index()

print("\nCountry Summary from Pandas:")
print(country_summary)
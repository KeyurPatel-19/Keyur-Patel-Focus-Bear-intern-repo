import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create database connection
engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

print("✅ Connected to PostgreSQL")

# -------------------------------
# 1. Fetch all users
# -------------------------------
query_all = "SELECT * FROM users;"
df_users = pd.read_sql(query_all, engine)

print("\nAll Users:")
print(df_users)

# -------------------------------
# 2. Active users only
# -------------------------------
query_active = """
SELECT name, email, country, subscription_type
FROM users
WHERE is_active = TRUE;
"""

df_active = pd.read_sql(query_active, engine)

print("\nActive Users:")
print(df_active)

# -------------------------------
# 3. Data Transformation
# -------------------------------

# Count users by country
country_count = df_users.groupby("country").size()

print("\nUsers per country:")
print(country_count)

# Filter premium users
premium_users = df_users[df_users["subscription_type"] == "Premium"]

print("\nPremium Users:")
print(premium_users)

# Add new column
df_users["user_status"] = df_users["is_active"].apply(
    lambda x: "Active" if x else "Inactive"
)

print("\nUpdated Data:")
print(df_users)
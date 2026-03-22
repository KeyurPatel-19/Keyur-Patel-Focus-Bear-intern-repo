import pandas as pd

# Load dataset
df = pd.read_csv("sample_data.csv")

# Show first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Show basic information
print("\nDataset information:")
print(df.info())

# Filter rows where Age is greater than 25
filtered_df = df[df["Age"] > 25]
print("\nPeople older than 25:")
print(filtered_df)

# Sort by Salary in descending order
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nSorted by Salary (highest to lowest):")
print(sorted_df)

# Group by Department and calculate average salary
grouped_df = df.groupby("Department")["Salary"].mean()
print("\nAverage salary by department:")
print(grouped_df)

# Fill missing Age values with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Replace incorrect department name
df["Department"] = df["Department"].replace("Hr", "HR")

# Drop rows with missing Name values
cleaned_df = df.dropna(subset=["Name"])

print("\nCleaned dataset:")
print(cleaned_df)

# Pivot table example
pivot_df = df.pivot_table(values="Salary", index="Department", aggfunc="mean")
print("\nPivot table:")
print(pivot_df)
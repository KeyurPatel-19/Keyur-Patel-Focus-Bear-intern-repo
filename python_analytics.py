import pandas as pd

# Load dataset
data = pd.read_csv("sample_data2.csv")

# Print dataset
print("Dataset:\n")
print(data)

# Show basic info
print("\nSummary:")
print(data.describe())
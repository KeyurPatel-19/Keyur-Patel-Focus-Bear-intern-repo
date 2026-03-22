import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
days = [1, 2, 3, 4, 5]
active_users = [120, 150, 170, 160, 200]

features = ["Focus Mode", "Break Timer", "Task List", "Habit Tracker"]
usage = [80, 65, 90, 70]

study_hours = [1, 2, 3, 4, 5, 6, 7]
productivity_score = [50, 55, 60, 68, 72, 78, 85]

# Line Chart
plt.figure(figsize=(8, 5))
plt.plot(days, active_users, marker="o", color="blue")
plt.title("Daily Active Users")
plt.xlabel("Day")
plt.ylabel("Number of Users")
plt.grid(True)
plt.show()

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(features, usage, color="green")
plt.title("Feature Usage Count")
plt.xlabel("Features")
plt.ylabel("Usage")
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, productivity_score, color="red")
plt.title("Study Hours vs Productivity")
plt.xlabel("Study Hours")
plt.ylabel("Productivity Score")
plt.show()

# Data for Seaborn
df = pd.DataFrame({
    "Focus_Sessions": [2, 3, 4, 4, 5, 6, 7, 8, 8, 9],
    "Breaks_Taken": [5, 4, 4, 3, 3, 2, 2, 2, 1, 1],
    "Productivity": [50, 55, 60, 63, 68, 74, 78, 82, 85, 90]
})

# Histplot
plt.figure(figsize=(8, 5))
sns.histplot(df["Productivity"], bins=5, kde=True, color="purple")
plt.title("Distribution of Productivity Scores")
plt.xlabel("Productivity Score")
plt.ylabel("Frequency")
plt.show()

# Heatmap
plt.figure(figsize=(8, 5))
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
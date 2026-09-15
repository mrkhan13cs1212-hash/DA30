import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Arun", "Sneha", "Kiran", "Anjali", "Ravi", "Neha", "Rahul"],
    "Age": [20, 21, None, 22, 21, 20, None, 21, 20],
    "Marks": [78, 92, 56, None, 67, 95, 39, 73, 78],
    "Attendance": [85, 94, 72, 91, None, 96, 65, 82, 85]
}
df = pd.DataFrame(data)

print("Final Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Highest Attendance:", df["Attendance"].max())
print("Highest Attendance:", df["Attendance"].mean())

top_student = df.loc[df["Marks"].idxmax()]

print(top_student)

print("List of Students who has sored More", df.loc[df["Marks"] >= 75])

print(df.loc[df["Marks"] >= 75])

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

# Round values
df["Age"] = df["Age"].round(2)
df["Marks"] = df["Marks"].round(2)
df["Attendance"] = df["Attendance"].round(2)

# Check cleaned data
print("CLEANED DATA:")
print(df)

print("Highest Attendance:", df["Attendance"].max())
print("Highest Attendance:", df["Attendance"].mean())

print("Students who scored 75 or above:")
print(df.loc[df["Marks"] >= 75])

print("Students who Attended below 75 classes:")
print(df.loc[df["Attendance"] < 75])

print("High Performing Students:")
print(df.loc[(df["Marks"] >= 75) & (df["Attendance"] >= 85)])

high_performers = df.loc[
    (df["Marks"] >= 75) & (df["Attendance"] >= 85)
]

print("Number of High Performers:", len(high_performers))

df.to_csv("cleaned_students.csv", index=False)
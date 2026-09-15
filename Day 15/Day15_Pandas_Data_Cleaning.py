import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Arun", "Sneha", "Kiran", "Anjali", "Ravi", "Neha", "Rahul"],
    "Age": [20, 21, None, 22, 21, 20, None, 21, 20],
    "Marks": [78, 92, 56, None, 67, 95, 39, 73, 78],
    "Attendance": [85, 94, 72, 91, None, 96, 65, 82, 85]
}

df = pd.DataFrame(data)

print(df)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

print(df[df.duplicated()])

df = df.drop_duplicates()
print(df.shape)
print(df)
print("Duplicate rows:", df.duplicated().sum())

print("Average Age:", df["Age"].mean())
print("Average Marks:", df["Marks"].mean())
print("Average Attendance:", df["Attendance"].mean())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

df["Age"] = df["Age"].round(2)
df["Marks"] = df["Marks"].round(2)
df["Attendance"] = df["Attendance"].round(2)

print(df)

print(df.isnull().sum())
print(df.isnull().sum())
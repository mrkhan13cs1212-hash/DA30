import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Arun", "Sneha", "Kiran", "Anjali", "Ravi", "Neha"],
    "Age": [20, 21, 20, 22, 21, 20, 22, 21],
    "Marks": [78, 92, 56, 88, 67, 95, 39, 73],
    "Attendance": [85, 94, 72, 91, 78, 96, 65, 82]
}

df = pd.DataFrame(data)

print("====Basic Analysis====")
print(df)
print(df.head())
print(df.tail(3))
print(df.info())
print(df.describe())
print(df.shape)

print("\n====Column Analysis====")
print(df[df.columns[0]])
print("====Marks===")
print(df[df.columns[2]])
print("Average Marks: ",df[df.columns[2]].mean())
print("Highest Marks: ", df[df.columns[2]].max())
print("Lowest Marks: ", df[df.columns[2]].min())

print("\n====Filtering====")
print("Students who scored 75 or above")
print(df[df[df.columns[2]] >= 75])
print("Students whose attendance is below 75%")
print(df[df[df.columns[3]] < 75])
print("Students who passed")
print(df[df[df.columns[2]] >= 40])
print("Students who failed")
print(df[df[df.columns[2]] < 40])

print("\n====Mini Analyst====")
print("Students who scored 75 or above AND have attendance of 85 or above")
print(df[(df[df.columns[2]] >= 75) & (df[df.columns[3]] >= 85)])
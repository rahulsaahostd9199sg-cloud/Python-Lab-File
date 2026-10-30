# Program based on Pandas
import pandas as pd

data = {
    "Roll No": [1, 2, 3, 4, 5],
    "Name": ["Aman", "Rahul", "Priya", "Neha", "Sara"],
    "Marks": [85, 72, 90, 65, 78]
}
df = pd.DataFrame(data)

print("===== Student Data =====")
print(df)
print("\n===== Data Analysis =====")
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Total Marks:", df["Marks"].sum())

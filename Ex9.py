# Simple Data Analysis

n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    mark = float(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

if n > 0:
    total = sum(marks)
    average = total / n
    print("\n===== Data Analysis =====")
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))
else:
    print("Please enter at least one student.")

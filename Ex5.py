# Student Report Card Generator

name = input("Enter your name: ")
roll = input("Enter your roll number: ")
subjects = ["English", "Maths", "Science", "Social Studies", "Hindi"]
marks = []

for subject in subjects:
    marks.append(int(input(f"Enter marks for {subject}: ")))

total = sum(marks)
percentage = total / len(subjects)

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
else:
    grade = "F"

result = "Pass" if percentage >= 50 else "Fail"
print("\n----- Student Report Card -----")
print("Name:", name)
print("Roll No:", roll)
for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)

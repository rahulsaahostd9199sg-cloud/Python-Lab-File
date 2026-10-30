# Conditional if, nested if, else and elif statements
# if statement
num = int(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# elif statement for grades
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Nested if statement
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 21:
        print("Eligible for driving and heavy vehicle license")
    else:
        print("Eligible for driving license")
else:
    print("Not eligible for driving license")

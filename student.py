# Building Python Modules, Obtaining User Data and Printing Desired Output

# File: mymodule.py
def display(name, roll):
    print("\n----- Student Details -----")
    print("Student Name:", name)
    print("Roll Number:", roll)

# File: student.py
import mymodule

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
mymodule.display(name, roll)

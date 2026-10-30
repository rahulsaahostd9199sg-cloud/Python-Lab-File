# Iteration using loops and data structures: strings, lists, tuples, sets and dictionaries
print("For loop:")
for i in range(1, 6):
    print(i)

print("\nWhile loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

print("\nString:")
for ch in "Python":
    print(ch, end=" ")
print("\nList:")
for n in [1, 2, 3, 4, 5]:
    print(n, end=" ")
print("\nTuple:")
for name in ("Aman", "Priya", "Neha"):
    print(name)
print("Set:")
for colour in {"Red", "Green", "Blue"}:
    print(colour)
print("Dictionary:")
student = {"Name": "Rahul Kumar", "Course": "MCA", "Semester": 3}
for key, value in student.items():
    print(key, ":", value)

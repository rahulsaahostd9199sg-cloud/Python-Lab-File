# Percentage distribution of expenses using a Matplotlib pie chart

import matplotlib.pyplot as plt

categories = ["Rent", "Food", "Transport", "Education",
              "Entertainment", "Savings"]
expenses = [8000, 5000, 2000, 3000, 1500, 4500]

print("===== Monthly Expenses =====")
for category, amount in zip(categories, expenses):
    print(category, ": ₹", amount)
print("Total Expenses: ₹", sum(expenses))

plt.figure(figsize=(7, 7))
plt.pie(expenses, labels=categories, autopct="%1.1f%%", startangle=90)
plt.title("Expense Distribution")
plt.axis("equal")
plt.tight_layout()
plt.show()

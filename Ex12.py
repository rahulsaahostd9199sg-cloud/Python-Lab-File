# Visualize monthly sales data using a Matplotlib bar chart

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 28000, 35000, 40000, 38000]

print("===== Monthly Sales Data =====")
for month, amount in zip(months, sales):
    print(month, ": ₹", amount)

plt.figure(figsize=(8, 5))
plt.bar(months, sales, edgecolor="black")
plt.title("Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales (in ₹)")
plt.tight_layout()
plt.show()

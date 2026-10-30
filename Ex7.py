# Calculate and display total bill for items using user input

total_bill = 0.0
n = int(input("Enter number of items: "))

for i in range(n):
    print("\nEnter details of item", i + 1)
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    amount = quantity * price
    total_bill += amount
    print("Amount for", name, "=", round(amount, 2))

print("\n========== BILL ==========")
print("Total Bill = ₹", round(total_bill, 2))
print("==========================")

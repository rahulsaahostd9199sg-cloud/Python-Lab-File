# Weekly Temperature Data Analysis and Visualization

import matplotlib.pyplot as plt
import numpy as np

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [32, 34, 31, 35, 36, 33, 30]
temp = np.array(temperature)

print("===== Weekly Temperature Data =====")
for day, value in zip(days, temperature):
    print(day, ":", value, "°C")

print("\n===== Data Analysis =====")
print("Average Temperature:", round(np.mean(temp), 2), "°C")
print("Highest Temperature:", np.max(temp), "°C on", days[np.argmax(temp)])
print("Lowest Temperature:", np.min(temp), "°C on", days[np.argmin(temp)])

plt.figure(figsize=(8, 5))
plt.plot(days, temperature, marker="o", linestyle="-")
plt.title("Weekly Temperature Analysis")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

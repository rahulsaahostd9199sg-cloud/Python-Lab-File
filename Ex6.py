# User-defined modules and standard/library modules

# File: mycalc.py
def add(a, b):
    return a + b

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# File: library_demo.py
import mymodule
import random
import sys
import math
import string
import numpy as np
from scipy import constants
from scipy.special import comb

print("Square:", math.sqrt(2))
print("Factorial of 5:", math.factorial(5))
print("Random integer:", random.randint(1, 100))
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Pi:", constants.pi)
print("5C2:", comb(5, 2))
print("Python version:", sys.version.split()[0])
print("Square root of 16:", math.sqrt(16))
print("Lowercase letters:", string.ascii_lowercase)
values = [5, 2, 9, 1]
values.append(7)
values.sort()
print("Sorted list:", values)

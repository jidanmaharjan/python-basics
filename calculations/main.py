# Division is decimal by default
print(5 / 2)  # Output: 2.5

# Integer division uses //
print(5 // 2)  # Output: 2

#negative numbers will round down
print(-5 // 2)  # Output: -3

# fix round down
print(int(-5 / 2))  # Output: -2

# modular division uses %
print(10 % 3)  # Output: 1

# negative number modular division uses %
print(-10 % 3)  # Output: 2

# consistent with other languages
import math
print(math.fmod(-10, 3))  # Output: -1

# more math helper
print(math.ceil(5.2))  # Output: 6
print(math.floor(5.8))  # Output: 5
print(math.trunc(5.8))  # Output: 5
print(math.pow(2, 3))  # Output: 8.0
print(math.sqrt(16))  # Output: 4.0
print(math.factorial(5))  # Output: 120


# Max min int
float('inf') # Positive infinity
float('-inf') # Negative infinity

# Python numbers are infinite so they never overflow
import math
print(math.pow(10, 1000))  # Output: 1e+1000

# this large number is less than infinity 
print(math.pow(10, 1000) < float('inf'))  # Output: True
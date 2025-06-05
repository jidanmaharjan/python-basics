# Tuples are immutable sequences in Python, which means once they are created, their elements cannot be changed.
# They are similar to lists but have some key differences, such as being hashable and allowing for faster access.
# Tuples can be used as keys in dictionaries, while lists cannot.

tup = (1, 2, 3)  # Creating a tuple
print(tup)  # Output: (1, 2, 3)
print(tup[0])  # Accessing the first element: Output: 1
print(tup[1:])  # Slicing the tuple: Output: (2, 3)
print(len(tup))  # Getting the length of the tuple: Output: 3
print(tup[-1])  # Accessing the last element: Output: 3


# Can be used as keys in dictionaries
myMap = {(1,2): 3}
print(myMap)  # Output: {(1, 2): 3}
print(myMap[(1, 2)])  # Accessing value using tuple key: Output: 3

mySet = set()
mySet.add((1, 2))  # Adding a tuple to a set
print(mySet)  # Output: {(1, 2)}

# Lists can't be keys in dictionaries or elements in sets
myMap[[3,4]] = 5  # This will raise a TypeError
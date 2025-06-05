# Hashset 

mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)  # {1, 2}

print(len(mySet))  # 2

print(1 in mySet)  # True
print(3 in mySet)  # False

mySet.remove(1)  # Remove an element
print(mySet)  # {2}

mySet.add(2)  # Adding an existing element has no effect
print(mySet)  # {2}

# list to set
myList = [1, 2, 3, 4, 5]
mySetFromList = set(myList)  # Convert list to set
print(mySetFromList)  # {1, 2, 3, 4, 5}

# Set comprehension
mySetComp = {x for x in range(10) if x % 2 == 0}  # Create a set of even numbers
print(mySetComp)  # {0, 2, 4, 6, 8}
# Arrays are called lists in Python 
arr = [1, 2, 3, 4, 5]
print(arr)

# Can be used as a stack
arr.append(6)  # Add an element to the end
print(arr)
arr.pop()  # Remove the last element
print(arr)

arr.insert(0, 0)  # Insert an element at the beginning
print(arr)

# Inserting in middle is  BigO(n) operation
arr.insert(3, 3.5)  # Insert an element at index 3
print(arr)

# Indexing and assign the value is O(1)
arr[2] = 2.5  # Change the value at index 2
print(arr)

n=5
arra = [1] * n
print(arra)  # Create an array of size n with all elements initialized to 1

print(arr[-1])  # Access the last element
print(arr[-2]) # Access the second last element

# Slicing the array
print(arr[1:4])  # Get elements from index 1 to 3 (4 is exclusive)

# Unpacking the array
a, b, c, *rest = arr  # Unpack first three elements and rest into a list
print(a, b, c)  # Prints first three elements
print(rest)  # Prints the rest of the elements


# Loop through the array
for i in arr:
    print(i)  # Print each element in the array


for i in range(len(arr)):
    print(arr[i], end=' ')  # Print each element using index


print('\n')

for i, n in enumerate(arr):
    print(f'Index: {i}, Value: {n}')  # Print index and value of each element


#reversing the array
arr.reverse()  # Reverse the array in place
print(arr)


#sorting the array
unsorted_arr = [5, 2, 9, 1, 5, 6]
unsorted_arr.sort()  # Sort the array in place
print(unsorted_arr)

unsorted_arr.sort(reverse=True)  # Sort the array in descending order
print(unsorted_arr)


# sorting strings
str_arr = ['banana', 'apple', 'cherry', 'date', 'elderberry']
str_arr.sort()  # Sort the array of strings in alphabetical order
print(str_arr)

# Custom sorting by length
str_arr.sort(key=lambda x: len(x))  # Sort by length of strings
print(str_arr)

# List comprehension
list_comp = [x**2 for x in range(10)]  # Create a list of squares of numbers from 0 to 9
print(list_comp)

# Filtering with list comprehension
filtered_list = [x for x in range(20) if x % 2 == 0]  # Create a list of even numbers from 0 to 19
print(filtered_list)

# 2D lists
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Create a 2D list
print(two_d_list)

# 2D list using loop
new_two_d_list = [[0]*4 for i in range(3)]  # Create a 3x4 2D list initialized with 0
print(new_two_d_list)

# This wont work
new_two_d_list = [[0]*4] * 3  # This creates a 2D list with references to the same inner list
print(new_two_d_list)
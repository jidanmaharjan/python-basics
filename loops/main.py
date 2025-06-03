# while loops are similar
n=0 
while n < 5:
    print('n = ', n)
    n += 1


# for loops are similar but use range
for n in range(5):
    print('n = ', n)

# range can be defeined with start, stop, step
for n in range(1, 10, 2):
    print('n = ', n)

# can be decremented
for n in range(10, 0, -2):
    print('n = ', n)

# Arrays = lists in Python
# Lists are dynamic arrays
# for loops can iterate over lists
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print('name = ', name)

# Lists can be indexed
print('First name = ', names[0])

# Lists can be sliced
print('First two names = ', names[:2])  # Slicing from start to index 2 (exclusive)

# Objects = dictionaries in Python
# Dictionaries are key-value pairs
# for loops can iterate over dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f'{key} = {value}')
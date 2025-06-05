# Hashmap aka dictionary, a collection of key-value pairs, objects in javascript
# Hashmaps are mutable, meaning you can change them in place
# They are unordered, meaning the order of elements is not guaranteed
# They are indexed by keys, not by integers like lists

myMap = {}
myMap['key1'] = 'value1'
myMap['key2'] = 'value2'
myMap['key3'] = 12
myMap['key4'] = [1, 2, 3]

print(myMap)  # {'key1': 'value1', 'key2': 'value2', 'key3': 12, 'key4': [1, 2, 3]}

#change a value
myMap['key1'] = 'newValue1'
print(myMap)  # {'key1': 'newValue1', 'key2': 'value2', 'key3': 12, 'key4': [1, 2, 3]}

# searching values
print('key1' in myMap)  # True
print('key5' in myMap)  # False

# Accessing values
print(myMap['key1'])  # newValue1

# removing a key-value pair
myMap.pop('key2')
print(myMap)  # {'key1': 'newValue1', 'key3': 12, 'key4': [1, 2, 3]}

# Manually inserting key-value pairs
myMap= {'key5': 'value5', 'key6': 'value6'}
print(myMap)  # {'key5': 'value5', 'key6': 'value6'}


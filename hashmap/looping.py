#Looping through a hashmap

myMap = {'key1': 'value1',
          'key2': 'value2',}

for key in myMap:
    print(f"Key: {key}, Value: {myMap[key]}")

for val in myMap.values():
    print(f"Value: {val}")

for key, val in myMap.items():
    print(f"Key: {key}, Value: {val}")


# Strings are similar to arrays
s= "abc"
print(s[0])  # a
print(s[1])  # b

print(s[0:2])

# They are immutable, meaning you cannot change them in place
try:
    s[0] = 'A'  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

# So, modifying a string requires creating a new string
s+= "def"  # Concatenation creates a new string
print(s)  # abcdef

#Strings can be converted
print(int("123")+int("123"))  # Convert strings to integers and add them

# Numbers can be converted to strings
print(str(123) + str(456))  # Convert integers to strings and concatenate them

# Get ASCII value of a character
print(ord('A'))  # Get ASCII value of 'A'
print(chr(65))  # Get character from ASCII value 65

# Combine list of strings into a single string
# with an empty string delimitor
words = ['Hello', 'World']
sentence = ''.join(words)  # Combine without spaces
print(sentence)  # HelloWorld



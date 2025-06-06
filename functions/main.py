def outer(a,b):
    def inner(c):
        return a + b + c
    return inner

print(outer(1,2)(3))  # Output: 6
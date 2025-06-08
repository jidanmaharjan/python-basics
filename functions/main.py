def outer(a,b):
    def inner(c):
        return a + b + c
    return inner

print(outer(1,2)(3))  # Output: 6


# Can modify objects but not reassign
# unlsess using nonlocal keyword

def double(arr, val):
    def helper():
        for i,n in enumerate(arr):
            arr[i] *=2

        # will only modify val in helper scope
        # val *=2

        # this will modify val in outer scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1,2,3]
val = 10
double(nums, val)
# Output: [2, 4, 6] 20

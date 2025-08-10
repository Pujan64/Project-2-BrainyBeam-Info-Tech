import numpy as np
def square_plus_one(x):
    return x**2 + 1

my_ufunc = np.frompyfunc(square_plus_one, 1, 1)

# create an array
arr = np.array([5,9,10,4])

# apply the custom ufunc
result = my_ufunc(arr)

print("original array:", arr)
print("after applying custom ufunc:", result)

# find the smallest element from the given array.

array = [ 15, 26, -54678, -5, -7, -9294542, 16, 15 ]
smallest = array[0]

for num in array:
    if num < smallest :
        smallest = num
print(f"{smallest} is the smallest element")

# method 2
print(f"the smallest element from the array is {min(array)}")

# method 3
small = array.sort()
print(f"the smallest element is {array[0]}")      
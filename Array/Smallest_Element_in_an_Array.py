# find the smallest element from the given array.

array = [ 15, 26, -54678, -5, -7, -9294542, 16, 15 ]

smallest = array[0]

for num in array:
    if num < smallest :
        smallest = num
print(f"{smallest} is the smallest element")
           
        
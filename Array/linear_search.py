# linear search - Linear search is a method of finding elements within a list. It is also called a sequential search. It is the simplest searching algorithm.

array = [ 15, 26, 67 ,5, 92, 16, 15 ]
element = int(input("Enter the element = "))

length = len(array)

for i in range(length) :
    if array[i] == element : 
        print(f"element {element} is on index {i} in array")
        break
else :
    print(f"element {element} is not in array")    


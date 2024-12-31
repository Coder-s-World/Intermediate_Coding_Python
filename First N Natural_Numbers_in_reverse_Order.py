# print first n natural numbers in reverse order
# using for loop
# Ex. n= 5 -- output 5 4 3 2 1

n =  int(input("enter the number = "))

for i in range(n, 0,-1):
    print(i, end =" ")
print(" ")    

# using while loop

m = int(input("enter the number = "))
temp = m
while temp >= 1:
    print(temp, end = " ")
    temp = temp-1
    
    
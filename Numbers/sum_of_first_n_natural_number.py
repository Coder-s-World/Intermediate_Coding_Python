# print sum of first n natural number

# method 1 - using for loop

# Ex.  num = 5 -- 1+2+3+4+5 = 15
num = int(input("Enter number = "))
res = 0

for i in range(1,num+1):
    res = i + res
print(res)
    
# using while loop
num2 = int(input("Enter number = "))
result = num2 * (num2+1) // 2
print(result)

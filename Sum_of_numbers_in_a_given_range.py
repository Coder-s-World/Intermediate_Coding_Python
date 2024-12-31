# code  Sum of numbers in a given range 

n= int(input("enter min number : "))
m = int(input("enter max number : "))
res = 0

for i in range(n,m+1):
    res = res + i
print(res)
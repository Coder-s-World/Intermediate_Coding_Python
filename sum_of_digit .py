# addition of number 
# ex - 234 is 2 + 3 + 4 = 9

num = int(input("enter the number : "))

res = 0

while num != 0 :
    rem = num % 10
    res = rem + res 
    num = num // 10
print(res)

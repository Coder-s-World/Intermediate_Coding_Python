# reversing to the number 
# ex 234 - 432

n = int (input("enter the number : "))
rev = 0

while n != 0 :
    rem = n % 10
    rev = rev * 10 + rem
    n = n// 10
print(rev) 
    
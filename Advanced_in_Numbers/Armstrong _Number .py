# armstromg number = In Python, an Armstrong number is a number that equals the sum of its individual digits, each raised to the power of the number of digits.


n = int(input("Enter the number : "))
temp = n

n_string = str(temp)
length = len(n_string)
sum = 0

while temp != 0 :
    rem = temp % 10
    sum = rem ** length + sum
    temp = temp // 10
print("sum = ",sum)
    
if n == sum : 
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not armstrong number")

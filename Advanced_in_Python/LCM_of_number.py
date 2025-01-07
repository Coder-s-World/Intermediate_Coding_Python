# LCM = Least Common Multiple(LCM) is a method to find the smallest common multiple between any two or more numbers.
# 16 → 16, 32, 48, 64, (80),… 
# 20 → 20, 40, 60, (80),…, 
# We can see that the first common multiple for both numbers is 80

# formula to find is : LCM (a,b) = (a x b)/GCD(a,b)
# firstly we will find HCF then using that only easily get LCM

n1 = int(input("enter first number : "))
n2 = int(input("enter second number : "))

minimum = min(n1,n2)

for num in range(1,minimum+1):
    if n1 % num == 0 and n2 % num == 0 :
        HCF = num
    
LCM = (n1 * n2) / HCF

print(f"LCM of {n1} and {n2} is {LCM}") 
# HCF = Highest Common Factor
# GCD = Greatest Common Divisor

# In Prime factor program we learnt how to find the factor and also what is factor of number, so in this program we will learn how to find out the common factor of 2 numbers and amonng that factor which is the highest factor common in both numbers factor.

# steps to find HCF/GCD
#   1. accept two numbers as n1 and n2
#   2. find which number is lowest n1 or n2 using min function
#   3. initialize 'for' loop with range upto lowest number
#   4. check if both the number is divisible by same number
#   5. if divisor is same then print on console and update HCF value by every ietration 
#   7. once for loop range stop program exits and print HCF

n1 = int(input("enter first number : "))
n2 = int(input("enter second number : "))

minimum = min(n1,n2)

for num in range(1,minimum+1):
    if n1 % num == 0 and n2 % num == 0 :
        HCF = num
        
print(f"{HCF} is the HCF/GCD")      
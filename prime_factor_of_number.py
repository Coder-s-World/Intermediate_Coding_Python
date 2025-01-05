# Here we will find prime factor of number 

# To find prime factor of number fistly we should understand what is prime number  and factor

# Prime number - number which is divisible by either 1 or number it self
# Factor - Factors are the numbers that can divide a number exactly.  Hence, after division, there is no remainder left.
# 18 = 2 * 3 * 3 (here, factor are always prime number that's why it is called as prime factor of number)


num = int(input(" Enter the number : ")) 
smallest_prime = 2 
print("prime factor of number are : ", end="")

while num > 1 :                          # This is because any number greater than 1 can potentially have prime factors.
    if num % smallest_prime == 0 :       # If it is divisible, it means smallest_prime is a factor of num.
        print(smallest_prime, end = " ") # If smallest_prime is a factor, it is printed to the console.
        num = num // smallest_prime      # This line updates num by dividing it by smallest_prime, effectively removing that factor from num. 
    else:
        smallest_prime += 1              # If num is not divisible by smallest_prime, this else block is executed, incrementing smallest_prime by 1 to check the next potential prime number.
    


          
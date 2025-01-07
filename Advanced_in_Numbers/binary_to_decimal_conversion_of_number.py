# binary number - A binary number is a number expressed in the base-2 numeral system
# decimal number - A decimal is a number that consists of a whole and a fractional part.

binary_num = int(input("enter binary number : "))
i = 0
calc = 0
base = 2

while binary_num != 0 :
    rem = binary_num % 10 
    calc = pow(base,i) * rem + calc
    i += 1
    binary_num //= 10
    
print(f"{calc} is the conversion of binary to decimal number")


















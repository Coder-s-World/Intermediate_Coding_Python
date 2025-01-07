# octal - An octal number is a number in a base-8 numeral system that uses the numbers 0 through 7

binary_num = int(input("enter binary number : "))
i = 0
calc = 0
base = 8 

while binary_num != 0 :
    rem = binary_num % 10 
    calc = pow(base,i) * rem + calc
    i += 1
    binary_num //= 10
    
print(f"{calc} is the conversion of octal number to decimal number")




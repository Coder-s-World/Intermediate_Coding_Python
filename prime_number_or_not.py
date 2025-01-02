# prime number are those number which is only divisible by either 1 or number it self.

# Note - 0 and 1 is not prime number

# To check that divide each number with that particular number if it is divisible by more than number other than  1 or number itself than it is prime number.

# input from user
n = int(input("enter the number : "))
count = 0


# logic
for i in range (2,n+1):
    if n % i == 0:
        count = count + 1
         
# output statement     

if n < 2 :
    print("invalid number") 
elif count == 1 :        
    print("number is prime")
else:
    print("number is not prime")



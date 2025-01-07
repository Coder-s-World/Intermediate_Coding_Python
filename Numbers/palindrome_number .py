# palindrome number = A given number can be said palindromic in nature if the reverse of the given number is the same as that of a given number
# ex = 121 is palindrome number

num = int(input("enter the number : "))
temp = num
rev = 0

while temp != 0 :
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp // 10
print(rev)

if num == rev :
    print(f"{num} is palindrome number")
else:
    print(f"num is not palindrome number")
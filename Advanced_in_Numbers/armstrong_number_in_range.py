# print armstrong number from the given range

low = int(input("Enter the lowest number of range  = "))
high = int(input("Enter the highest number of range  = "))


for num in range(low, high+1):
    temp = num
    string = str(temp)
    length = len(string)
    sum = 0 
    
    while temp != 0 :
        rem = temp % 10
        sum = sum + rem ** length
        temp = temp // 10
        
    if num == sum :
        print(num , end = " ")
        

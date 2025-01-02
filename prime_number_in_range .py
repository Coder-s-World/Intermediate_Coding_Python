# check which numbers in given range is prime number

min = int(input("enter intial number of range : ")) 
max =  int(input("enter ending number of range : "))

for num in range( min, max + 1 ):
    if num > 1:
        for iter in range( 2 , num ):
            if num %  iter == 0:
                break 
        else:
            print( num, end = " ")
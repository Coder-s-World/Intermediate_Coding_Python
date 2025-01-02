# leap year = one year in every four, in which February has 29 days instead of 28(366 days in a year)

# how it calculated - Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

year =  int(input("enter the year : "))

if ( year % 400 == 0 )or ( year % 4 == 0 and year % 100 != 0 ):
    print(f"{year} is lear year")
else:
    print(f"{year} is not leap year")
    
    
leap_year = 2012

if (leap_year % 400 == 0) or (leap_year % 4 == 0 and leap_year % 100 != 0):
    print("This is a Leap Year")
else:
    print("This is not a Leap Year")
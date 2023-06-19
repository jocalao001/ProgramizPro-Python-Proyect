#!/usr/bin/python3
year = int(input('write the year to check if is a leap year or not: '))
 
# If year is divisible by 4 and not divisible by 100
# or if year is divisible by 400, it's a leap year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    result = 'leap year'
 
# all other remaining years are not a leap year
else:
    result = 'not a leap year'
 
print(result)

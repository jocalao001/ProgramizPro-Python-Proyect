#!/usr/bin/python3
number = int(input('put a number to the table of  multiplication: '))
 
# iterate a loop from 1 to 5
for i in range(1, 6):
 
    # compute product in each iteration of the loop
    product = number * i
    print(number, '*', i, '=', product)

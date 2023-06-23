#!/usr/bin/python3
# create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# use for loop to iterate through numbers list
# inside the loop, only print the odd items on the list
for num in numbers:
    if num % 2 != 0:
        print(num)
    else:
        continue

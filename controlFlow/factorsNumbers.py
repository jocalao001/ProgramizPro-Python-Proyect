#!/usr/bin/python3
number = int(input())

# create a for loop that iterates from 1 to number
for i in range (1, number + 1):
    # check if number is perfectly divisible (remainder 0)
    # If yes, print i
    if number % i == 0:
        print(i)

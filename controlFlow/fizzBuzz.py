#!/usr/bin/python3
number = int(input())

# check if number is multiple of both 3 and 5
if(number % 3 == 0 and number % 5 == 0):
    print("FizzBuzz")

# check if number is multiple of 3
elif (number % 3 == 0):
    print("Fizz")

# check if number is multiple of 5
elif(number % 5 == 0):
    print('Buzz')

else:
    print(number)

#!/usr/bin/python3
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))


# check for smallest number using if...elif...else statement 
if (number1 < number2 and number1 < number3):
    print(number1)

elif (number2 < number1 and number2 < number3 ):
    print(number2)

else: 
    print(number3)

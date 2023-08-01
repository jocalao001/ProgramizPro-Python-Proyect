# Lambda functions is just like a regular function with couple of differences:
# a lambda function doesn't have name
# the body of a lambda function can have only one expression

double = lambda n, b: (n * 2) + b
print(double(10, 5))  # 20


# Get the user two number, and call the function double()
n = int(input("put a number: "))
b = int(input("put a second number: "))
suma_multi = double(n, b)
print(suma_multi)


# Create a lambda function that returns the square of a number passed as an argument.
import math

# create the function
poweroftwo = lambda b: math.pow(b, 2)
squareroot = lambda n: math.sqrt(n)

# take user input
number1 = float(input("put a number to squareroot: "))
number2 = float(input("put a number to pow by 2: "))

# call the function and print the result
print(squareroot(number1))
print(poweroftwo(number2))

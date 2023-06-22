#!/usr/bin/python3
num1 = int(input())
num2 = int(input())

# create a function my_function that accepts are two arguments arg1 and arg2
def my_function(arg1, arg2):

    # compare arg1 and arg2 to see if they are equal
    if arg1 == arg2:
        return True
    else:
        return False

# call the function and pass the parameters
Description = my_function(num1, num2)
print(Description)

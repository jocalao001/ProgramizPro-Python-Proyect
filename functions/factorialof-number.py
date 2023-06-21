#!/usr/bin/python3
def compute_factorial(n):
    factorial = 1
    
    # computer factorial
    for i in range(1, n+1):
        factorial = factorial * i 
    
    # return factorial
    return factorial

# get user input
number = int(input())
total = compute_factorial(number)

print(total)

#!/usr/bin/python3
def compute_sum(number):

    total = 0
    
    # iterate loop from 1 to number
    for i in range(1, number+1):
        total = total + i
    
    return total

n1 = int(input('put a number: '))
total = compute_sum(n1)
print(total) 


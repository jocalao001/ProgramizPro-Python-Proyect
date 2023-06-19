#!/usr/bin/python3
# The initial value of total is 0
total = 0
print('Warning: ¡remember that zero number terminates the loop!') 
while True:
    
    number = int(input('Enter a number: '))
    # If number is negative, don't add that number to total    
    if number < 0:
        continue
    
    # If number is zero, terminate the loop
    if number == 0:
        break
    
    total = total + number
 
print('Total: ', total)

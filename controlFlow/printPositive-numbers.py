#!/usr/bin/python3
# run a while loop that is always True
while(True):
    # take integer input for number 
    number = int(input())
    
    # check if user input is less than 0. If yes, skip the number
    if number < 0:
        continue

    # check if user input is 0. If yes, terminate the loop
    if number == 0:
        break
  
    # print the number
    print(number)

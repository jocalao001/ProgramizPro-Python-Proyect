#!/usr/bin/python3
def get_largest_number(n1, n2, n3):
 
    # return n1 if it's the largest number
    if n1 > n2 and n1 > n3:
        return n1
 
    # return n2 if it's the largest number
    elif n2 > n1 and n2 > n3:
        return n2
   
    # else return n3
    else:
        return n3

def get_shortest_number(n1, n2, n3):
 
    # return n1 if it's the shortest number
    if n1 < n2 and n1 < n3:
        return n1
 
    # return n2 if it's the shortest number
    elif n2 < n1 and n2 < n3:
        return n2
   
    # else return n3
    else:
        return n3


n1 = int(input('put one number: '))
n2 = int(input('put another number: '))
n3 = int(input('put the last number: '))

largest_number = get_largest_number(n1, n2, n3)
print('the largest number is: ',largest_number)   
 
shortest_number = get_shortest_number(n1, n2, n3)
print('the shortest number is: ',shortest_number)    

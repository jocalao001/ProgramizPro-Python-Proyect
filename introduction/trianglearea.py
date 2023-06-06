#!/usr/bin/python3
# get three sides of the triangle from the user
# store them in variables a, b and c
a = float(input('introduce the first side: '))
b = float(input('introduce the second side: '))
c = float(input('introduce the last side: '))

# compute semiperimeter s
s = (a+b+c)/2

# compute area and print it
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('the area of the triangle is: ' ,area)

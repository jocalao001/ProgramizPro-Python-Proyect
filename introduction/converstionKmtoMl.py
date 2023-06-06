#!/usr/bin/python3
# Program to convert distance in kilometer to miles
# The distance will be entered by the user.

# getting distance in kilometers
# and converting it to its equivalent floating-point number

km = float(input('Enter distance in km: '))

# conversion ratio

km_miles_ratio = 0.621

# computing distance in miles
miles = km * km_miles_ratio
print('Distance in miles:', miles)

#!/usr/bin/python3
# get input value for total number of friends 
total_friends = float(input('add how many people: '))

# get input value for total bill 
total_bill = float(input('add the cost of the bill: '))

# calculate the tax amount
percent = float(input('add the percent tax: '))

percenttaxamount = percent / 100
tax = total_bill + (total_bill * percenttaxamount)

# divide bill among friends
splitAmount = tax / total_friends

# print the split amount
print( 'each person will pay: ', splitAmount, ' soles')

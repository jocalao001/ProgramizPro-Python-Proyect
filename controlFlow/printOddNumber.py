# get integer input from the user
n = int(input())

# loop from 1 to n (n should be inclusive) 
for number in range(1, n + 1):

    # if number is an odd number, print it
    if number % 2 == 0:
        print(number)

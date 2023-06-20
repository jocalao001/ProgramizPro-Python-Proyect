#!/usr/bin/python3
n = int(input())

# run a for loop from 1 to n
for i in range (1, n + 1):
    # check whether i is divisible by 3
    if i % 3 == 0:
        # if yes, skip the current iteration
        continue
    # print value of i
    print(i)

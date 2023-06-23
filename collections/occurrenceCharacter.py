#!/usr/bin/python3
# take string input for string1
string1 = input()

# take character input for character1
character1 = input()

count = 0

# use for loop to iterate through string1
for i in string1:
    # check if character is present in the string or not
    if i == character1:
        count += 1
print(count)

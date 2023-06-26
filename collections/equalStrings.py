#!/usr/bin/python3
# take string input for str1 and str2
str1 = input()
str2 = input()

# convert str1 and str2 to lowercase and compare them
str01 = str1.lower()
str02 = str2.lower()
if str01 == str02:
    print('Equal')
else:
    print('Not Equal')

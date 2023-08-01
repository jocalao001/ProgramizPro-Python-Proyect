
n = int(input())
numbers = [3*i for i in range(1, n+1)]

# creating an empty dictionary
# square_numbers = {}
# # using a loop to add items to dictionary
# for number in numbers:
#     square_numbers[number] = number**2

# create dictionary using comprehension
square_numbers = {number*2:number*3 for number in numbers}
#Dictionary Comprehension With Condition
square_numbers2 = {number*2:number*3 for number in numbers if number >= 2}
square_numbers3 = {number*2:number*3 for number in numbers if number % 2 == 0}

print(square_numbers)
print(square_numbers2)
print(square_numbers3)

# Create a dictionary using dictionary comprehension.
# get integer input
b = int(input())

# create the dictionary using comprehension
numbers = {number:number*10 for number in range(1, b+1) if number >= 3}
print(numbers)

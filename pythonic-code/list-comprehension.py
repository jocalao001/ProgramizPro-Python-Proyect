# get an integer input
n = int(input())

# create a list using list comprehension
numbers = [5*i for i in range(1, n+1)]
even_numbers = [i for i in numbers if i % 2 == 0]
odd_numbers = [i for i in numbers if i % 2 != 0]
# print the list
print(numbers)
print(even_numbers)
print(odd_numbers)

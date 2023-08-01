def add_numbers(*numbers):
    # calculate sum of tuple items
    total = 0
    for number in numbers:
        total = total + number

    return total


# call add_numbers with two arguments
result = add_numbers(5, 10)
print(result)  # 15

# call add_numbers with three arguments
result = add_numbers(5, 10, 20)
print(result)  # 35

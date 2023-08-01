# def display_info(name, age):
#     print(f"name = {name}")
#     print(f"age = {age}")
display_info2 = lambda x, y: print(f"name = {x}\nage = {y}")

# display_info(age="22", name="Amanda")
display_info2(y="22", x="Amanda")


# def greet(message):
#     print(message)
def greet1(message="hola"):
    print(message)


# greet("hola")
greet1()


def display(symbol="*", number=5):
    print(f"symbol = {symbol}")
    print(f"number = {number}")


print("When arguments are not passed.")
display()

print("When the first argument is passed.")
display("#")

print("When both arguments are passed.")
display("$", 5)


print('Hello','there') # Hello there
print('Hello','there', sep = ', ')  # Hello, there
print('Hello', 'there', sep = '###') # Hello###there

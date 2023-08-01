my_dict = {"a": "juice", "b": "grill", "c": "corn"}

# take user input for data
data = input()

# create a flag variable and set it to False
flag = False

# loop through my_dict
for key, value in my_dict.items():
    # check if the value entered by the user is in the dictionary or not
    # if yes, set flag to True and terminate the loop
    if value == data:
        flag = True
        break

# print value found not found based on the flag status
if flag == True:
    print("Value found")
else:
    print("Value not found")

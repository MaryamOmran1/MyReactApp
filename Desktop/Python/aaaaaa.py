all_user_inputs = [ ]
user_input = input("Enter a number: ")

while user_input != "#":
    if user_input in all_user_inputs:
        print("The number " + user_input + " is duplicated.")
    else:
        all_user_inputs.append(user_input)
    
    user_input = input("Enter a number: ")

print(all_user_inputs)
print("Bye..")
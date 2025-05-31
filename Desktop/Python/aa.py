number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

multi = int(number1) * int(number2)

if multi <= 1000:
    print("The result is ", multi)
else:
    print(int(number1) + int(number2))
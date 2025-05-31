list1 = [ ]
number = float(input("Enter your numbers: "))

while number != 0:
    list1.append(number)
    number = float(input("Enter your numbers: "))
    total = sum(list1)
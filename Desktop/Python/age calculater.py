import datetime
birthYear = int(input("Enter your birth year: "))
age = datetime.datetime.now().year - birthYear

print("Your age is ", age, "years old.")
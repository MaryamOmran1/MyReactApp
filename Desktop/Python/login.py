import getpass

database = {"Maryam": 12345, "Omran": 67890}
username = input("Enter your username: ")
password = getpass.getpass("Enter Your Password: ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
            print("Verfied!")
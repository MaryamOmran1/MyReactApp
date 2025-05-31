import random
n = random.randrange(1,10)
guess = int(input("Enter a number: "))
while n != int(guess):
    if int(guess) < n:
        print("Too Low")
        guess = int(input("Enter a number: "))
    elif int(guess) > n:
        print("Too High!")
        guess = int(input("Enter a number: "))
    else:
        break
print("you guessed it right!!")
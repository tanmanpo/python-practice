import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Guess a number from 1 to 100: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        break

import random

n = random.randint(1,100)

guess = int(input("Guess a number from 1-99: "))

while True:
    if guess > n:
        print("Guess is too high")
        guess = int(input("Guess a number from 1-99: "))
    elif guess < n:
        print("Guess is too low")
        guess = int(input("Guess a number from 1-99: "))
    else:
        print("You got it right!")
        ans = input("Do you want to try again?(Y/n): ").lower()
        if ans == "y":
            guess = int(input("Guess a number from 1-99: "))
        else:
            print("Goodbye!")
            break

import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Welcome to Number Guessing Game!")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess > secret_number:
        print("Too high!")

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Congratulations! You won!")
        print("Attempts used:", attempts)
        break

if attempts == max_attempts and guess != secret_number:
    print("Game over!")
    print("The secret number was:", secret_number)

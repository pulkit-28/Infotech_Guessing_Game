import random

secret_number = random.randint(1, 100)


guess = int(input("Guess the secret number between 1 and 100: "))


while guess != secret_number:
    if guess < secret_number:
        print("Sorry, your guess is too low.")
    else:
        print("Sorry, your guess is too high.")

    guess = int(input("Guess the secret number between 1 and 100: "))


print("You guessed the number!")
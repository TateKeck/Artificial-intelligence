# Programmer: Tate Keck
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI technology ")

import random
import time


def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 1000. Can you guess it?")

    # Generate a random number
    secret_number = random.randint(1, 1000)
    attempts = 0

    while True:
        guess = input("\nEnter your guess (or 'quit' to exit): ")

        if guess.lower() == 'quit':
            print("Thanks for playing!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts!")
            break

        # Adding a little delay for dramatic effect
        time.sleep(0.5)


if __name__ == "__main__":
    guessing_game()
# Programmer: Tate Keck
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI technology ")

import random

def choose_word():
    words = ["python", "hangman", "game", "computer", "programming", "banana", "cat", "dog"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")
            if attempts == 0:
                print("Sorry, you lost. The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
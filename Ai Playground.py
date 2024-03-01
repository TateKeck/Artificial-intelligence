# Programmer: Tate Keck
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI technology ")
import random


def generate_code(length):
    return [random.randint(1, 6) for _ in range(length)]


def evaluate_guess(code, guess):
    exact_matches = sum(1 for i in range(len(code)) if code[i] == guess[i])
    code_counts = [code.count(num) for num in set(code)]
    guess_counts = [guess.count(num) for num in set(guess)]
    near_matches = sum(
        min(code_count, guess_counts[num - 1]) for num, code_count in enumerate(code_counts, 1)) - exact_matches
    return exact_matches, near_matches


def main():
    code_length = 4
    max_attempts = 10
    code = generate_code(code_length)

    print("Welcome to Mastermind!")
    print("Try to guess the secret code.")
    print("The code consists of numbers between 1 and 6.")
    print(f"You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt}:")
        guess = [int(x) for x in input("Enter your guess (e.g., 1234): ") if x.isdigit()]

        if len(guess) != code_length:
            print("Invalid guess. Please enter exactly 4 digits.")
            continue

        exact_matches, near_matches = evaluate_guess(code, guess)

        if exact_matches == code_length:
            print("Congratulations! You guessed the code!")
            break

        print(f"Exact matches: {exact_matches}")
        print(f"Near matches: {near_matches}")

    else:
        print("Sorry, you ran out of attempts. The secret code was:", ''.join(map(str, code)))


if __name__ == "__main__":
    main()

# Programmer: Tate Keck
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI technology ")
def word_chain():
    print("Welcome to Word Chain!")
    print("Enter words where each word starts with the last letter of the previous word.")
    print("To quit the game, enter 'quit'.")

    prev_word = input("Enter the starting word: ").lower()
    if prev_word == 'quit':
        print("Game over.")
        return

    while True:
        next_word = input("Enter a word: ").lower()
        if next_word == 'quit':
            print("Game over.")
            break

        if next_word[0] != prev_word[-1]:
            print("Invalid word! Word must start with the last letter of the previous word.")
            continue

        prev_word = next_word

if __name__ == "__main__":
    word_chain()

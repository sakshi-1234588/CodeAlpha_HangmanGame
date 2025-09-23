import random

def hangman():
    words = ["python", "hangman", "simple", "coding", "random"]
    word = random.choice(words)
    guessed = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("_ " * len(word))

    while attempts > 0:
        current = ""
        for ch in word:
            current += ch + " " if ch in guessed else "_ "
        print("\nWord:", current.strip())

        if all(ch in guessed for ch in word):
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)

    else:
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()

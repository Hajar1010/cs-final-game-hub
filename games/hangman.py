# hangman guess the word
# Author: hajar1010
# Description: the player guesses the word letter by letter
import random

def play_hangman():
    from project import normalize_word
    word_list = ["python", "banana", "coding", "giraffe", "keyboard"]
    word = normalize_word(random.choice(word_list))
    guessed_word = ["_"] * len(word)
    attempts = 6

    print("Welcome to Hangman!")
    while attempts > 0 and "_" in guessed_word:
        print("Word:", " ".join(guessed_word))
        guess = input(f"You have {attempts} attempts left. Guess a letter: ").lower()
        guess = normalize_word(guess)

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")

    if "_" not in guessed_word:
        print("Congratulations, you guessed the word:", word)
    else:
        print("Sorry, you lost. The word was:", word)

# 🎲 Word Scrambler Game
# Author: hajar1010
# Description: Scrambles a word and asks the user to guess the original.

import random

def play_word_scramble():
    from project import normalize_word, scramble_word
    """
    Runs the Word Scrambler game:
    - Picks a random word from a list
    - Scrambles it
    - Asks the user to guess
    - Tracks score across rounds
    """
    print("I'll scramble a word and you have to guess the original.")

    score = 0
    words = [
        "python", "banana", "coding", "giraffe", "keyboard", "whiteboard", "television",
        "functions", "school", "capybara", "planet", "rocket", "window", "coffee",
        "laptop", "umbrella", "elephant", "backpack", "triangle", "notebook",
        "sandwich", "building", "airplane", "reptile", "calendar", "awkward",
        "rhythm", "pneumonia", "jazz", "zodiac", "mystery", "phantom", "illusion",
        "treasure", "blizzard"
    ]

    while True:
        word = random.choice(words)
        word = normalize_word(word)  # ensure lowercase & letters only
        scrambled = scramble_word(word)
        print("\n________________________________________")
        print("Ohh I got you the best word!!")
        print("Here is the scrambled word:", scrambled)

        guess = input("Can you guess the original word? \nYour guess: ").strip().lower()

        if normalize_word(guess) == word:
            score += 10
            print(f"BINGOO!! You got it right 🎉 Your score: {score}")
        else:
            print(f"Oops, not quite. The word was '{word}'. Your score: {score}")

        again = input("That was fun! Wanna play again? (yes/no): ").strip().lower()
        if again != "yes":
            print(f"Alrightt, final score: {score}")
            print("Well, that was a good game!")
            break

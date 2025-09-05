import random
import re
from games.hangman import play_hangman
from games.scramble import play_word_scramble
from games.quiz import play_quiz

def main():
    menu=["Hangman", "Word Scramble", "Quiz", "Exit"]
    print("*** Welcome To The Game Hub ***")
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item}")
    print("*******************************")

    while True:
        game = input("what we are feeling today! choose from the menu: ").strip().lower()
#    - Call the corresponding function for the chosen game.
        if game=="hangman" or game=="1":
            play_hangman()
        elif game=="word scramble"  or game=="2":
            play_word_scramble()
        elif game=="quiz" or game=="3":
            play_quiz()
        elif game=="exit" or game=="4":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Enter a valid game")


def normalize_word(word):
    """
        Normalize a word by:
        - Converting to lowercase
        - Removing non-letter characters (punctuation, numbers, etc.)
        """
    return re.sub(r'[^a-z]', '', word.lower())

def scramble_word(word, seed=None):
    """
        Scramble the letters of a word.
        Returns a string with letters shuffled."""
    letters = list(word)
    if seed is not None:
        random.seed(seed)
    random.shuffle(letters)
    return "".join(letters)

def score_quiz(correct, total, elapsed_seconds):
    """
        Calculate a quiz score:
        - Base score: percentage of correct answers
        - Optional penalty for time taken (e.g., 1% per 30 seconds)
        - Max score capped at 100, min score 0
        """
    if total <= 0:
        raise ValueError("Total questions must be greater than 0")

    base_score = (correct / total) * 100
    penalty = (elapsed_seconds // 30)  # 1% penalty per 30 seconds
    final_score = max(0, min(100, int(base_score - penalty)))
    return final_score

if __name__ == "__main__":
    main()

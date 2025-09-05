# Game Hub Project


## Author
Hajar Essalihi
GitHub: [hajar1010](https://github.com/hajar1010)
edX: HE_2509_SEF9
Location: Taroudant,Morocco
Date Recorded: 02/09/2025

---

## Project Overview
The **Game Hub** project is a Python-based application that serves as a collection of three mini-games: **Hangman**, **Word Scramble**, and a **Quiz game**. The primary goal of this project is to consolidate multiple small Python programs into a single organized, and modular program, allowing the user to select and play any of the available games from a central menu. This project demonstrates the use of Python functions, modular file structure, standard libraries, and simple game logic while also emphasizing reusable code and testable functions.

The Game Hub provides a menu-driven interface where users can navigate between games, track their scores, and enjoy an interactive experience. Each game has been implemented in a separate Python file within a `games` folder, making it easy to expand the hub with additional games in the future.

---

## File Structure and Functionality

- **`project.py`**
  This is the main entry point of the application. It contains the `main()` function, which displays the menu to the user and repeatedly prompts for a game selection until the user chooses to exit. The file also includes three top-level functions required for CS50P testing:
  1. `normalize_word(word)` – Converts a word to lowercase and removes non-letter characters, useful for validating guesses in Hangman or Word Scramble.
  2. `scramble_word(word, seed=None)` – Returns a shuffled version of a word. The optional `seed` parameter allows for deterministic shuffling, which is helpful when writing tests with pytest.
  3. `score_quiz(correct, total, elapsed_seconds)` – Calculates a quiz score based on correct answers, total questions, and time taken. Scores are capped between 0 and 100 with an optional penalty for elapsed time.

- **`games/hangman.py`**
  Implements the Hangman game. Users guess one letter at a time, and correct guesses reveal the letter’s positions in the word. Incorrect guesses reduce the remaining lives. The game continues until the user either completes the word or runs out of attempts. The words are selected randomly from a predefined list.

- **`games/scramble.py`**
  Implements the Word Scramble game. A word is selected randomly from a predefined list and its letters are scrambled. The user attempts to guess the original word. Correct guesses increase the score, while incorrect guesses prompt feedback and allow the user to try again or exit.

- **`games/quiz.py`**
  Implements the Quiz game. The game contains multiple categories, each with multiple-choice questions. The user answers by typing the letter corresponding to their chosen option. The game tracks the number of correct answers and provides a final score at the end. The scoring system can be enhanced using the `score_quiz` function.

- **`requirements.txt`**
  Lists all pip-installable libraries needed for the project. In this project, only Python standard libraries are used (`random` and `re`), so this file can remain empty or include a note stating that no external libraries are required.

- **`test_project.py`**
  Contains pytest tests for the three top-level functions in `project.py`. Tests validate that `normalize_word` correctly removes symbols and converts letters to lowercase, `scramble_word` shuffles letters correctly and deterministically with a seed, and `score_quiz` calculates scores accurately under different scenarios.

---

## Design Choices
Several design choices were made to balance simplicity, modularity, and testability. Each game is implemented in its own file to maintain a modular structure, making the code easier to maintain and extend. The main menu in `project.py` centralizes user interaction, allowing users to select games without editing code. The top-level functions were designed to be **reusable and testable**, meeting CS50P’s requirements for pytest validation. Additionally, the Word Scramble function includes an optional seed to allow reproducible tests, demonstrating attention to software testing best practices.

---

## Conclusion
The Game Hub project demonstrates foundational Python programming skills, including functions, modules, user input handling, loops, and basic game logic. It emphasizes modularity, reusability, and testability while providing a fun interactive experience. The project is structured to allow easy expansion with additional games or features, such as a leaderboard, timers, or category selection in the quiz. Overall, this project consolidates multiple Python concepts into a single cohesive program suitable for both learning and demonstration purposes.


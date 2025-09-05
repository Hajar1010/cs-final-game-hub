# quiz.py
# Author: hajar1010
#description: a quiz app the user choisses the category and tries to select the correct answer
import random

questions = {
    "math": [
        {"question": "What is 7 × 8?", "options": ["A. 54", "B. 56", "C. 58", "D. 60"], "answer": "B"},
        {"question": "What is the square root of 64?", "options": ["A. 6", "B. 7", "C. 8", "D. 9"], "answer": "C"},
        {"question": "What is 12 divided by 3?", "options": ["A. 2", "B. 3", "C. 4", "D. 5"], "answer": "C"},
        {"question": "What is 9 squared?", "options": ["A. 81", "B. 72", "C. 99", "D. 108"], "answer": "A"}
    ],
    "geography": [
        {"question": "What is the capital of Japan?", "options": ["A. Seoul", "B. Tokyo", "C. Kyoto", "D. Osaka"], "answer": "B"},
        {"question": "Which ocean is on the west coast of the U.S.?", "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"], "answer": "C"},
        {"question": "Which country has the Eiffel Tower?", "options": ["A. Spain", "B. Italy", "C. France", "D. Germany"], "answer": "C"},
        {"question": "What continent is Egypt in?", "options": ["A. Asia", "B. Africa", "C. Europe", "D. South America"], "answer": "B"}
    ],
    "science": [
        {"question": "What planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"], "answer": "B"},
        {"question": "What gas do plants absorb from the air?", "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "answer": "C"},
        {"question": "How many legs do insects have?", "options": ["A. 4", "B. 6", "C. 8", "D. 10"], "answer": "B"},
        {"question": "What’s H2O more commonly known as?", "options": ["A. Salt", "B. Oxygen", "C. Water", "D. Hydrogen"], "answer": "C"}
    ],
    "technology": [
        {"question": "What does 'CPU' stand for?", "options": ["A. Central Processing Unit", "B. Computer Power Unit", "C. Central Programming Utility", "D. Control Processing Unit"], "answer": "A"},
        {"question": "What company created the iPhone?", "options": ["A. Google", "B. Apple", "C. Microsoft", "D. Samsung"], "answer": "B"},
        {"question": "What does 'HTML' stand for?", "options": ["A. Hyper Transfer Markup Language", "B. HyperText Markup Language", "C. HighText Machine Language", "D. Hyperlink Text Marking Language"], "answer": "B"},
        {"question": "Which of these is not a programming language?", "options": ["A. Python", "B. Java", "C. Windows", "D. C++"], "answer": "C"}
    ],
    "history": [
        {"question": "Who was the first President of the United States?", "options": ["A. Abraham Lincoln", "B. George Washington", "C. Thomas Jefferson", "D. John Adams"], "answer": "B"},
        {"question": "In what year did World War II end?", "options": ["A. 1940", "B. 1943", "C. 1945", "D. 1948"], "answer": "C"},
        {"question": "Which ancient civilization built the pyramids?", "options": ["A. Romans", "B. Greeks", "C. Egyptians", "D. Mayans"], "answer": "C"},
        {"question": "Who discovered America in 1492?", "options": ["A. Marco Polo", "B. Christopher Columbus", "C. Ferdinand Magellan", "D. Vasco da Gama"], "answer": "B"}
    ]
}


def play_quiz():
    from project import score_quiz
    """
    Play the quiz game. Prompts the user to choose a category,
    asks questions, and keeps track of the score.
    """
    print("\nWelcome to the Quiz Game!")
    print("Available categories:", ', '.join(questions.keys()))

    score = 0
    total_questions = 0

    # Ask user for category
    while True:
        category = input("Choose a category: ").strip().lower()
        if category in questions:
            break
        else:
            print("Invalid category. Please choose from the list above.")

    # Copy and shuffle questions
    question_list = questions[category][:]
    random.shuffle(question_list)

    # Track start time for optional timing penalties
    import time
    start_time = time.time()

    # Ask each question
    for q in question_list:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        total_questions += 1
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {q['answer']}")
        print(f"Current score: {score}")
    elapsed = time.time() - start_time
    final_score = score_quiz(score, total_questions, int(elapsed))
    print(f"\nGame over! You took {elapsed.__round__(2)} seconds and your final scoreis: {final_score}")

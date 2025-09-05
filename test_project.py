from project import normalize_word
from project import scramble_word
from project import score_quiz
import pytest

def test_normalize_word():
    assert normalize_word("")==""
    assert normalize_word("Hello!") == "hello"
    assert normalize_word("123Python") == "python"

def test_scramble_word():
    assert scramble_word("")==""
    word = "python"
    scrambled1 = scramble_word(word, seed=42)
    scrambled2 = scramble_word(word, seed=42)
    assert scrambled1 == scrambled2

def test_score_quz():
    assert score_quiz(3, 5, 0) == 60
    assert score_quiz(5, 5, 30) == 99

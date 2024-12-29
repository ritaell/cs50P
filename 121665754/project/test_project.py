import pytest
from project import add_word, take_quiz, view_progress

# Test add_word function
def test_add_word():
    words = {}

    def mock_input(prompt):
        responses = {"Enter a new word: ": "hello", "Enter the meaning: ": "a greeting"}
        return responses[prompt]

    add_word.input = mock_input
    add_word(words)

    assert "hello" in words
    assert words["hello"] == {"meaning": "a greeting", "correct": 0, "attempts": 0}

# Test take_quiz function
def test_take_quiz():
    words = {
        "hello": {"meaning": "a greeting", "correct": 0, "attempts": 0}
    }

    def mock_input(prompt):
        return "a greeting"

    take_quiz.input = mock_input
    take_quiz(words)

    assert words["hello"]["correct"] == 1
    assert words["hello"]["attempts"] == 1

# Test view_progress function
def test_view_progress(capsys):
    words = {
        "hello": {"meaning": "a greeting", "correct": 1, "attempts": 2},
        "world": {"meaning": "the earth", "correct": 0, "attempts": 1}
    }

    view_progress(words)
    captured = capsys.readouterr()

    assert "hello: 1/2 correct (50.00% accuracy)" in captured.out
    assert "world: 0/1 correct (0.00% accuracy)" in captured.out

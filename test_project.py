import pytest
from unittest.mock import patch
from project import (
    play_again,
    score_quiz, 
    quiz_level,
    start_quiz,
    questions_level
)

def test_play_again(): 
    """Test play_again function"""

    with patch("builtins.input", return_value="yes"):
        assert play_again() is True
    with patch("builtins.input", return_value ="no"):
        assert play_again() is False

def test_quiz_level():
    """Test quiz_level function"""

    with patch("builtins.input", return_value="1"):
        assert quiz_level("") == "1"
    with patch("builtins.input", return_value="exit"):
        with pytest.raises(SystemExit) as e:
            quiz_level("")
        assert e.type == SystemExit
    with patch("builtins.input", return_value="2"):
        assert quiz_level("") == "2"
    with patch("builtins.input", return_value="3"):
        assert quiz_level("") == "3"
    
def test_questions_level():
    """Test questions_level function"""

    assert questions_level("1") == [
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "O2"],
        "answer": "H2O",
    },
    {
        "question": "What's the capital of Spain?",
        "options": ["London", "Madrid", "Berlin"],
        "answer": "Madrid",
    },
    {
        "question": "Which country gifted the Statue of Liberty to the US?",
        "options": ["Germany", "England", "France"],
        "answer": "France",
    },
]
    assert questions_level("2") ==  [
    {
        "question": "Which European country has the longest coastline?",
        "options": ["Italy", "Greece", "Norway"],
        "answer": "Norway",
    },
    {
        "question": "What was the name of the Greek god of war?",
        "options": ["Ares", "Apollo", "Zeus"],
        "answer": "Ares",
    },
    {
        "question": "In which part of your body would you find the cruciate ligament?",
        "options": ["Knee", "Elbow", "Foot"],
        "answer": "Knee",
    },
]
    assert questions_level("3") == [
    {
        "question": "What is the driest desert in the world?",
        "options": ["Sahara Desert", "Atacama Desert", "Gobi Desert"],
        "answer": "Atacama Desert",
    },
    {
        "question": " In which year did the first modern Olympic Games take place?",
        "options": ["1886", "1896", "1906"],
        "answer": "1896",
    },
    {
        "question": "Which element has the highest melting point?",
        "options": ["Tungsten", "Titanium", "Platinum"],
        "answer": "Tungsten",
    },
]


def test_start_quiz(capsys):
    """Tests start_quiz function."""

    quiz_questions = [{
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2"],
            "answer": "H2O",
        }
    ]
    with patch("builtins.input", return_value="1"):
        start_quiz(quiz_questions)
        captured = capsys.readouterr()
        assert "Correct!" in captured.out

    with patch("builtins.input", return_value="2"):
        start_quiz(quiz_questions)
        captured1 = capsys.readouterr()
        assert "Wrong! The correct answer is: H2O" in captured1.out


def test_score_quiz(capsys):
    """Test score_quiz function."""
    
    score_quiz(1, 3)
    captured = capsys.readouterr()
    assert "Your score is 1/3" in captured.out
    assert "Your final grade is 33%" in captured.out



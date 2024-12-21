import pytest
from unittest.mock import patch
from game.gaming import gaming_setup
from game.training import training_setup
from game.general import begin

# Mocking the input function to simulate user input
def mock_input(prompt):
    responses = {
        "First choose a language | Primero, elige un lenguaje | Primer escull una llengua : ": "english",
        "Lowest number: ": "1",
        "Highest number: ": "10",
        "You can play training (0) mode or game (1) mode: ": "0",
        "Invalid input. Please enter a number or 'q' to quit.": "5",
        "Invalid input. Please enter a number or 'q' to quit.": "q"
    }
    return responses.get(prompt, "5")

# Test for gaming_setup function
@patch('builtins.input', side_effect=mock_input)
def test_gaming_setup():
    with patch('builtins.print') as mocked_print:
        gaming_setup(0)  # Testing in English
        mocked_print.assert_any_call("This is gaming mode, all types of arithmetic operators can appear (+,-,*).")
        mocked_print.assert_any_call("")  # Check for empty line
        mocked_print.assert_any_call("")  # Check for empty line after low/high input

# Test for training_setup function
@patch('builtins.input', side_effect=mock_input)
def test_training_setup():
    with patch('builtins.print') as mocked_print:
        training_setup(0)  # Testing in English
        mocked_print.assert_any_call("")  # Check for empty line after setup

# Test for begin class
@patch('builtins.input', side_effect=mock_input)
def test_begin_class():
    game = begin()
    language = game.start()
    assert language == 0  # Check if the language is set to English
    with patch('builtins.print') as mocked_print:
        game.welcome(language)
        mocked_print.assert_any_call("Hello, I'm your mental calculation trainer.")
        mocked_print.assert_any_call("If you want to stop at any moment, type 'q' and press enter.")
        mocked_print.assert_any_call("If you have any problems or you want to comment or suggest something, contact me at 'joanalnu5@gmail.com', thank you.")
        mocked_print.assert_any_call("")  # Check for empty line

# You can add more tests for other functions as needed

if __name__ == "__main__":
    pytest.main()
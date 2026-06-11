import pytest

from lib.grammar_checker import grammar_checker

def test_grammar_checker_returns_string_if_already_valid():
    result = grammar_checker("That'll do, Pig.")
    assert result == "That'll do, Pig."

def test_grammar_checker_adds_capital_letter():
    result = grammar_checker("in case I don't see ya: good afternoon, good evening and goodnight.")
    assert result == "In case I don't see ya: good afternoon, good evening and goodnight."

def test_grammar_checker_for_sentence_enders():
    result = grammar_checker("That'll do, Pig")
    assert result == "That'll do, Pig."

def test_grammar_checker_for_capital_and_ending():
    result = grammar_checker("my cat's breath smells like cat food")
    assert result == "My cat's breath smells like cat food."

def test_grammar_checker_raises_error_for_empty_string():
    with pytest.raises(Exception) as e:
        grammar_checker("")
    error_message = str(e.value)
    assert error_message == "Can't check string; it may be empty or invalid."

def test_grammar_checker_raises_error_for_invalid_type():
    with pytest.raises(Exception) as e:
        grammar_checker(2)
    error_message = str(e.value)
    assert error_message == "Can't check string; it may be empty or invalid."

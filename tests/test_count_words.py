import pytest

from lib.count_words import count_words

'''
This function should return a number.
'''
def test_count_words_returns_num():
    result = count_words("hello")
    assert isinstance(result, int)

'''
This function should return the number of words in the string.
'''
def test_count_words_returns_str_word_count():
    result = count_words("""I knew exactly what to do; 
                        but in a much more real sense, I had no idea what to do.""")
    assert result == 20

def test_count_words_throws_error_if_string_empty():
    with pytest.raises(Exception) as e:
        count_words("")
    error_message = str(e.value)
    assert error_message == "This text has no words for me to count!"
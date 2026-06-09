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
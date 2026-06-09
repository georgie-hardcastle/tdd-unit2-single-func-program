from lib.make_snippet import make_snippet

'''
The function should return a string.
'''
def test_make_snippet_returns_string():
    result = make_snippet("hello")
    assert isinstance(result, str)

'''
The function should return the first five words
of the string.
'''
def test_make_snippet_returns_1st_five_words():
    result = make_snippet("I'm not superstitious, but I am a little stitious.")
    assert len(result.split()) == 5

'''
The function should add '...' to the end of the truncated string.
'''
def test_make_snippet_adds_ellipsis_to_end_of_string():
    result = make_snippet("Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.")
    assert result == "Would I rather be feared..."
import random

from lib.calculate_reading_time import calculate_reading_time

def test_calculate_reading_time_for_200_wds():
    test_text = ' '.join(["word" for i in range(0, 200)])
    result = calculate_reading_time(test_text)
    assert result == "It will take approximately 1 minute to read this text."

def test_calculate_reading_time_for_400_wds():
    test_text = ' '.join(["word" for i in range(0, 400)])
    result = calculate_reading_time(test_text)
    assert result == "It will take approximately 2 minutes to read this text."

def test_calculate_reading_time_for_random_wds():
    test_text = ' '.join(["word" for i in range(0, 472955)])
    result = calculate_reading_time(test_text)
    assert result == "It will take approximately 2365 minutes to read this text."


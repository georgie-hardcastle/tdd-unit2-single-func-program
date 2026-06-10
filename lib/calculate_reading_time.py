import math

"""
Function name: reading_time

Arguments: one, a string

Returns: an estimate, in minutes (int), of how long it takes to read the given text.
"""
def calculate_reading_time(text):

    reading_time = math.ceil(len(text.split()) / 200)

    if reading_time > 1:
        return f"It will take approximately {reading_time} minutes to read this text."
    else:
        return f"It will take approximately {reading_time} minute to read this text."


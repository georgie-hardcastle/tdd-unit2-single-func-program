# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming I can read 200 words per minute.

## 2. Design the Function Signature

Function name: reading_time

Arguments: one, a string

Returns: an estimate, in minutes (int), of how long it takes to read the given text.

```python
# EXAMPLE

def reading_time(text):
    """
    Gives an estimate of reading time in minutes
    for a given text.

    Arguments: one string, "text"

    Returns: an estimate in minutes (int) of how long it takes to read
    the given text. 

    Side effects: none
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text containing exactly 200 words, 
it returns "It will take approximately 1 minute to read this text." 
"""
calculate_reading_time("... 200 ...") => "It will take approximately 1 minute to read this text."

"""
Given a text of 400 words,
it returns "It will take approximately 2 minutes to read this text."
"""
calculate_reading_time("... 400 ...") => "It will take approximately 2 minutes to read this text."

"""
Given a text of a random number, it returns
the same phrase as above with accurate reading time in minutes, rounded up to the nearest minute.
"""
calculate_reading_time("...547...") => "It will take approximately 3 minutes to read this text."


"""
Given an empty text, it throws an error.
"""
calculate_reading_time("") => "Can't calculate reading time for an empty text." 

"""
Given the wrong data type, it throws an error.
"""
calculate_reading_time(24) => "Can't calculate reading time for non-text data."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

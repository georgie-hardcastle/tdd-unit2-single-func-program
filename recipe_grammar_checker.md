# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

Function name: grammar_checker()

Arguments: one, a string, representing a sentence

Returns: the same string, with a capital letter at the beginning and a full stop at the end. 

```python
# EXAMPLE

def grammar_checker(text):
    """
    Given a string, check the first character of that string
    and if it is a lowercase letter, change it to uppercase.

    Check the final character of the string and if it is not a sentence-ending
    punctuation mark, add one

    Stretch goal: check the first word of the string, and if it is "how"
    "what "when" or "why", add a question mark to the end of the sentence
    instead of a full stop.
    """
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string, check the first character - if it is lowercase,
change it to uppercase.
"""
grammar_checker("in case I don't see ya: good afternoon, good evening and goodnight.") =>
"In case I don't see ya..."

"""
Check the final character in the string - if it is not a full stop,
exclamation point, or question mark - add a full stop. 
"""
grammar_checker("That'll do, Pig") => "That'll do, Pig." 

"""
Check the first word of the string - if it is a question-starting word,
add a question mark to the end of the sentence instead.
"""
grammar_checker("Why is the sky blue") => "Why is the sky blue?"

"""
If the string is empty, raise an error.
"""
grammar_checker("") => "No text to check." 

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
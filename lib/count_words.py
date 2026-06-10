def count_words(string):

    if not string:
        raise Exception("This text has no words for me to count!")

    return len(string.split())
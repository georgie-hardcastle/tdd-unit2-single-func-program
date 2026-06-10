def make_snippet(string):

    if not string:
        raise Exception("Can't truncate an empty string!")

    split_short_str = string.split()[0:5]

    return ' '.join(split_short_str) + '...'
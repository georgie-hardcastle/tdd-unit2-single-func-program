def make_snippet(string):

    split_short_str = string.split()[0:5]

    return ' '.join(split_short_str) + '...'
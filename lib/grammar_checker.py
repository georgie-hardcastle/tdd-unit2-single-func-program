def grammar_checker(string):

    if not isinstance(string, str):
        raise Exception("Can't check string; it may be empty or invalid.")
    
    if not string:
        raise Exception("Can't check string; it may be empty or invalid.")

    if string[0].isupper() and not string[-1].isalpha():
        return string
    elif string[0].isupper() and string[-1].isalpha():
        return string + "."
    elif string[0].islower() and not string[-1].isalpha():
        return string[0].upper() + string[1:]
    elif string[0].islower() and string[-1].isalpha():
        return string[0].upper() + string[1:] + "."
    else:
        raise Exception("Can't check string; it may be empty or invalid.")
    
    
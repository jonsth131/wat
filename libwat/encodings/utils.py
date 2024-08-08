import re
import string


def all_printable(value):
    return all(c in string.printable for c in value)


def run_func(text, func, pattern, name):
    if re.match(pattern, text):
        try:
            value = func(text).decode()
            return (name, value) if all_printable(value) else None
        except:
            return None
    else:
        return None

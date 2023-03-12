import re

from libwat.encodings.utils import all_printable


def insert_space_every_n(text, n):
    return ' '.join([text[i:i + n] for i in range(0, len(text), n)])


def from_bin(text):
    text = text.replace(' ', '')
    if len(text) % 8 != 0:
        return None
    text = insert_space_every_n(text, 8)
    result = convert(text, 2, r'^([01]{8} ?)*$')
    return f'Binary: {result}' if result is not None else None


def from_oct(text):
    result = convert(text, 8, r'^([0-9]{2,3} ?)*$')
    return f'Octal: {result}' if result is not None else None


def from_dec(text):
    result = convert(text, 10, r'^([0-9]{2,3} ?)*$')
    return f'Decimal: {result}' if result is not None else None


def from_hex(text):
    text = text.replace(' ', '')
    if len(text) % 2 != 0:
        return None
    text = insert_space_every_n(text, 2)
    result = convert(text, 16, r'^([a-fA-F0-9]{2} ?)*$')
    return f'Hex: {result}' if result is not None else None


def convert(text, base, pattern):
    if not re.match(pattern, text):
        return None

    try:
        result = ''.join([chr(int(v, base)) for v in text.split(' ')])
        return result if all_printable(result) else None
    except OverflowError:
        return None
    except ValueError:
        return None

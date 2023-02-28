import re

from libwat.encodings.utils import all_printable


def from_bin(text):
    result = convert(text, 2, r'^([01]{8} ?)*$')
    return f'Binary: {result}' if result is not None else None


def from_oct(text):
    result = convert(text, 8, r'^([0-9]{2,3} ?)*$')
    return f'Octal: {result}' if result is not None else None


def from_dec(text):
    result = convert(text, 10, r'^([0-9]{2,3} ?)*$')
    return f'Decimal: {result}' if result is not None else None


def from_hex(text):
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

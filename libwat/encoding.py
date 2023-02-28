from libwat.encodings import morse, base, number


def test_all(text):
    result = [
        base.check_b16(text),
        base.check_b32(text),
        base.check_b64(text),
        base.check_b85(text),
        morse.decode(text),
        number.from_bin(text),
        number.from_oct(text),
        number.from_dec(text),
        number.from_hex(text)
    ]

    return [i for i in result if i is not None]

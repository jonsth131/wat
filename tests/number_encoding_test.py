import unittest

from libwat.encodings import number


class BinaryEncodingTests(unittest.TestCase):
    def test_from_bin(self):
        result = number.from_bin('01110100 01100101 01110011 01110100')
        self.assertEqual(('Binary', 'test'), result)

    def test_from_bin_no_spaces(self):
        result = number.from_bin('01110100011001010111001101110100')
        self.assertEqual(('Binary', 'test'), result)

    def test_too_large(self):
        result = number.from_bin('11111111')
        self.assertEqual(None, result)

    def test_non_printable(self):
        result = number.from_bin('00000000')
        self.assertEqual(None, result)

    def test_invalid_input(self):
        result = number.from_bin('aaa')
        self.assertEqual(None, result)


class OctalEncodingTests(unittest.TestCase):
    def test_from_oct(self):
        result = number.from_oct('164 145 163 164')
        self.assertEqual(('Octal', 'test'), result)

    def test_too_large(self):
        result = number.from_oct('999')
        self.assertEqual(None, result)

    def test_non_printable(self):
        result = number.from_oct('10')
        self.assertEqual(None, result)

    def test_invalid_input(self):
        result = number.from_oct('aaa')
        self.assertEqual(None, result)


class DecimalEncodingTests(unittest.TestCase):
    def test_from_dec(self):
        result = number.from_dec('116 101 115 116')
        self.assertEqual(('Decimal', 'test'), result)

    def test_too_large(self):
        result = number.from_dec('999')
        self.assertEqual(None, result)

    def test_non_printable(self):
        result = number.from_dec('1')
        self.assertEqual(None, result)

    def test_invalid_input(self):
        result = number.from_dec('aaa')
        self.assertEqual(None, result)


class HexEncodingTests(unittest.TestCase):
    def test_from_hex(self):
        result = number.from_hex('74 65 73 74')
        self.assertEqual(('Hex', 'test'), result)

    def test_from_hex_no_spaces(self):
        result = number.from_hex('74657374')
        self.assertEqual(('Hex', 'test'), result)

    def test_too_large(self):
        result = number.from_hex('FF')
        self.assertEqual(None, result)

    def test_non_printable(self):
        result = number.from_hex('00')
        self.assertEqual(None, result)

    def test_invalid_input(self):
        result = number.from_hex('BOOM')
        self.assertEqual(None, result)

    def test_invalid_hex_string(self):
        result = number.from_hex('abcdef1234567890')
        self.assertEqual(None, result)


class BigIntEncodingTests(unittest.TestCase):
    def test_from_bigint(self):
        result = number.from_bigint('1952805748')
        self.assertEqual(('BigInt', 'test'), result)

    def test_too_large(self):
        result = number.from_bigint('999')
        self.assertEqual(None, result)

    def test_non_printable(self):
        result = number.from_bigint('1')
        self.assertEqual(None, result)

    def test_invalid_input(self):
        result = number.from_bigint('aaa')
        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()

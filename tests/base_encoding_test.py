import unittest

from libwat.encodings import base


class Base64Tests(unittest.TestCase):
    def test_b64(self):
        result = base.check_b64('dGVzdA==')
        self.assertEqual('Base64: test', result)

    def test_b64_invalid_returns_none(self):
        result = base.check_b64('AAAA')
        self.assertEqual(None, result)

    def test_b64_invalid_format_returns_none(self):
        result = base.check_b64('%$%')
        self.assertEqual(None, result)


class Base85Tests(unittest.TestCase):
    def test_b85(self):
        result = base.check_b85('bY*jN')
        self.assertEqual('Base85: test', result)

    def test_b85_invalid_returns_none(self):
        result = base.check_b85('AAAA')
        self.assertEqual(None, result)

    def test_b85_invalid_format_returns_none(self):
        result = base.check_b85('[]')
        self.assertEqual(None, result)


class Base32Tests(unittest.TestCase):
    def test_b32(self):
        result = base.check_b32('ORSXG5A=')
        self.assertEqual('Base32: test', result)

    def test_b32_invalid_returns_none(self):
        result = base.check_b32('AAAA')
        self.assertEqual(None, result)

    def test_b32_invalid_format_returns_none(self):
        result = base.check_b32('[]')
        self.assertEqual(None, result)


class Base16Tests(unittest.TestCase):
    def test_b16(self):
        result = base.check_b16('74657374')
        self.assertEqual('Base16: test', result)

    def test_b16_invalid_returns_none(self):
        result = base.check_b16('AAAA')
        self.assertEqual(None, result)

    def test_b16_invalid_format_returns_none(self):
        result = base.check_b16('[]')
        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()

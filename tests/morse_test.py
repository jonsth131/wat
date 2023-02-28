import unittest

from libwat.encodings import morse


class MorseTests(unittest.TestCase):
    def test_parse_morse(self):
        result = morse.decode('- . ... -')
        self.assertEqual('Morse: test', result)

    def test_parse_morse_ver2(self):
        result = morse.decode('_ . ... _')
        self.assertEqual('Morse: test', result)

    def test_invalid_code(self):
        result = morse.decode('________')
        self.assertEqual(None, result)

    def test_invalid_characters(self):
        result = morse.decode('aaa')
        self.assertEqual(None, result)

    def test_all_morse_characters(self):
        result = morse.decode(
            '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..')
        self.assertEqual('Morse: abcdefghijklmnopqrstuvwxyz', result)

    def test_all_morse_numbers(self):
        result = morse.decode(
            '----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.')
        self.assertEqual('Morse: 0123456789', result)

    def test_all_morse_characters_and_numbers(self):
        result = morse.decode(
            '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.')
        self.assertEqual('Morse: abcdefghijklmnopqrstuvwxyz0123456789', result)


if __name__ == '__main__':
    unittest.main()

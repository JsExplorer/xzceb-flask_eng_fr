import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('None'), 'Null') # test for null input
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test for correct translation

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('None'), 'Null') # test for null input
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test for correct translation

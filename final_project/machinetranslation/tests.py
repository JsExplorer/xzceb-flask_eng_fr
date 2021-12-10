import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testeng1(self):
        self.assertNotEqual(english_to_french(0), 0) # test for null input
    def testeng2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test for correct translation

class TestFrenchToEnglish(unittest.TestCase):
    def testfrench1(self):
        self.assertNotEqual(french_to_english(0), 0) # test for null input
    def testfrench2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test for correct translation

unittest.main()


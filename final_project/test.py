"""System module."""
import unittest
from translator import translate_french_to_english, translate_english_to_french

class Testf2e(unittest.TestCase):
    """ Test French to English Translator """
    def test_1(self):
        ''' test_1 '''
        self.assertEqual(translate_french_to_english('0'), '0')
        self.assertEqual(translate_french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(translate_french_to_english("None"), '')
        self.assertNotEqual(translate_french_to_english(0), 0)


class Teste2f(unittest.TestCase):
    """ Test English to French Translator """
    def test_2(self):
        ''' test_2 '''
        self.assertEqual(translate_english_to_french('0'), '0')
        self.assertEqual(translate_english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(translate_english_to_french("None"), '')
        self.assertNotEqual(translate_english_to_french(0), 0)

unittest.main()

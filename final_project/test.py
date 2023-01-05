"""System module."""
import unittest
from translator import translate_french_to_english, englishToFrench

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
    def test_2(self):englishToFrench
        ''' test_2 '''
        self.assertEqual(englishToFrench('0'), '0')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)

unittest.main()

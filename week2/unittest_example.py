import unittest
import truth

class TruthTest(unittest.TestCase):

    def test(self):
        self.assertTrue(truth.truthiness(1))

    def test_empty_string(self):
        self.assertRaises(StandardError, truth.truthiness, '')
if __name__ == '__main__':
    unittest.main()


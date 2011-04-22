import unittest
import truth

class TruthTest(unittest.TestCase):

    def test_basics(self):
        self.assertTrue(truth.truthiness(1))
        self.assertTrue(truth.truthiness(True))
        self.assertTrue(truth.truthiness('True'))

        self.assertFalse(truth.truthiness(0))
        self.assertFalse(truth.truthiness(False))
        self.assertFalse(truth.truthiness('False'))

    def test_actually_bool(self):
        import sys
        print sys.path
        self.assertTrue(True is truth.truthiness(1))

    def test_empty_string(self):
        self.assertRaises(StandardError, 
                        truth.truthiness, '')

if __name__ == '__main__':
    unittest.main()


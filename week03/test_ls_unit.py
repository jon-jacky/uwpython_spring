"""
Use os.system to test commands with command-line options in unittest
assert checks return status, should be 0 if command did not crash
"""

import unittest
import os

class LsTest(unittest.TestCase):

    def test_ls_l(self):
        """Test the command: ls -l"""
        status = os.system('ls -l')
        self.assertEqual(status, 0) # command returned success status to shell

    def test_ls_ltr(self):
        """Test the command: ls -ltr"""
        status = os.system('ls -ltr')
        self.assertEqual(status, 0)

if __name__ == '__main__':
    unittest.main()

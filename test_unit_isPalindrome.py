import unittest
import IsPalindrome


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(IsPalindrome.palindrome("Nurses run"),True)

    def test2(self):
        self.assertEqual(IsPalindrome.palindrome(22),True)

    def test3(self):
        self.assertEqual(IsPalindrome.palindrome(1),True)

    def test4(self):
        self.assertEqual(IsPalindrome.palindrome(),False)

if __name__ == '__main__':
    unittest.main(verbosity = 2)

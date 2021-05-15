import pytest
import IsPalindrome

class TestClass:
    def test_one(self):
        x = "Nurses run"
        assert IsPalindrome.palindrome(x) == True

    def test_two(self):
        x = 22
        assert IsPalindrome.palindrome(x) == True

    def test_three(self):
        x = 1
        assert IsPalindrome.palindrome(x) == True

    def test_four(self):
        assert IsPalindrome.palindrome() == False

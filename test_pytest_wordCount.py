import pytest
import WordCount
class TestClass:
    def test_one(self):
        x = "This is an activity"
        assert WordCount.wordCount(x) == 4

    def test_two(self):
        assert WordCount.wordCount() == 0

    def test_three(self):
        with pytest.raises(AttributeError):
            assert WordCount.wordCount(2)

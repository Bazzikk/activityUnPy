import unittest
import WordCount


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(WordCount.wordCount("This is an activity"),4)

    def test2(self):
        self.assertEqual(WordCount.wordCount(),0)

    def test3(self):
        with self.assertRaises(NameError):
            wordCount(2)

if __name__ == '__main__':
    unittest.main(verbosity = 2)

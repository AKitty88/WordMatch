import unittest
from word_ladder import find_shortest
from word_ladder import words


class TestWordLadder(unittest.TestCase):

    def test_word_normal_start_end(self):
        # Test with normal start and target word
        self.assertEqual(len(find_shortest("lead", "gold", words)), 4)

    def test_word_bad_start_normal_end(self):
        # Test with bad start and normal target word
        self.assertEqual(len(find_shortest("lsss", "gold", words)), 0)
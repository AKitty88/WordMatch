import unittest
from word_ladder_forTest import main_for_test

class TestWordLadder(unittest.TestCase):

    def test_short_with_normal_start_end(self):
        # Test the shortest path creator function with normal start and target word
        self.assertEqual(len(main_for_test("lead", "gold", "", "Y")), 4)

    def test_short_with_bad_start_normal_end(self):
        # Test the shortest path creator function with bad start and normal target word
        self.assertEqual(len(main_for_test("lsss", "gold", "", "y")), 0)
import unittest
from word_ladder_forTest import main_for_test

class TestWordLadder(unittest.TestCase):

    def test_short_good(self):
        # Test the shortest path creator function with normal start and target word
        self.assertEqual(len(main_for_test("lead", "gold", "", "Y")), 4)
        self.assertEqual(len(main_for_test("loss", "gold", "cold", "Y")), 5)

    def test_short_bad_start(self):
        # Test the shortest path creator function with bad start and normal target word
        self.assertEqual(len(main_for_test("lsss", "gold", "", "y")), 0)

    def test_short_bad_target(self):
        # Test the shortest path creator function with normal start and bad target word
        self.assertEqual(len(main_for_test("lead", "gggd", "", "Y")), 0)

    def test_short_different_length(self):
        # Test the shortest path creator function with normal start and target word that are not the same length
        self.assertEqual(len(main_for_test("lead", "gin", "", "y")), 0)
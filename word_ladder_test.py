import unittest
from word_ladder_forTest import main_for_test

class TestWordLadder(unittest.TestCase):

    def test_short_good_fourletters(self):
        # Test the shortest path creator function with four-letter-long normal start and target word
        self.assertEqual(len(main_for_test("lead", "gold", "", "Y")), 4)
        self.assertEqual(len(main_for_test("loss", "gold", "cold", "Y")), 5)
        self.assertEqual(len(main_for_test("loss", "gold", "loss", "Y")), 5)

    def test_short_good_threeletters(self):
        # Test the shortest path creator function with three-letter-long normal start and target word
        self.assertEqual(len(main_for_test("led", "god", "", "Y")), 3)
        self.assertEqual(len(main_for_test("led", "god", "ged", "Y")), 4)
        self.assertEqual(len(main_for_test("led", "god", "gin", "Y")), 3)

    def test_short_bad_start(self):
        # Test the shortest path creator function with bad start and normal target word
        self.assertEqual(len(main_for_test("lsss", "gold", "", "y")), 0)
        self.assertEqual(len(main_for_test("lsss", "gold", "cold", "y")), 0)
        self.assertEqual(len(main_for_test("lsss", "gold", "loss", "y")), 0)

    def test_short_bad_target(self):
        # Test the shortest path creator function with normal start and bad target word
        self.assertEqual(len(main_for_test("lead", "gggd", "", "Y")), 0)
        self.assertEqual(len(main_for_test("lead", "gggd", "cold", "Y")), 0)
        self.assertEqual(len(main_for_test("lead", "gggd", "loss", "Y")), 0)

    def test_short_different_length(self):
        # Test the shortest path creator function with normal start and target word that are not the same length
        self.assertEqual(len(main_for_test("lead", "gin", "", "y")), 0)
        self.assertEqual(len(main_for_test("lead", "gin", "tin", "y")), 0)
        self.assertEqual(len(main_for_test("lead", "gin", "lean", "y")), 0)

    def test_short_numbers(self):
        # Test the shortest path creator function with numbers
        self.assertEqual(len(main_for_test("45", "55", "", "Y")), 0)
        self.assertEqual(len(main_for_test("45", "55", "55", "Y")), 0)
        self.assertEqual(len(main_for_test("45", "55", "45", "Y")), 0)

    def test_short_float_numbers(self):
        # Test the shortest path creator function with float numbers
        self.assertEqual(len(main_for_test("45.05", "55.03", "", "Y")), 0)
        self.assertEqual(len(main_for_test("45.0566", "55.0566", "55", "Y")), 0)
        self.assertEqual(len(main_for_test("45.000", "55.999", "45", "Y")), 0)

#-----------------------------------------------------------------------------------------------------------------------

    def test_any_path_good_fourletters(self):
        # Test the any path creator function with four-letter-long normal start and target word
        self.assertEqual(len(main_for_test("lead", "gold", "", "N")), 4)
        self.assertEqual(len(main_for_test("loss", "toys", "cold", "N")), 3)
        self.assertEqual(len(main_for_test("loss", "gold", "loss", "N")), 7)

    def test_any_good_threeletters(self):
        # Test the any path creator function with three-letter-long normal start and target word
        self.assertEqual(len(main_for_test("led", "god", "", "jhf")), 3)
        self.assertEqual(len(main_for_test("led", "god", "ged", "jhf")), 7)
        self.assertEqual(len(main_for_test("led", "god", "gin", "jhf")), 3)

    def test_any_path_bad_start(self):
        # Test the any path creator function with bad start and normal target word
        self.assertEqual(len(main_for_test("lsss", "gold", "", "z")), 0)
        self.assertEqual(len(main_for_test("lsss", "gold", "cold", "z")), 0)
        self.assertEqual(len(main_for_test("lsss", "gold", "loss", "z")), 0)

    def test_any_path_bad_target(self):
        # Test the any path creator function with normal start and bad target word
        self.assertEqual(len(main_for_test("lead", "gggd", "", "")), 0)
        self.assertEqual(len(main_for_test("lead", "gggd", "cold", "")), 0)
        self.assertEqual(len(main_for_test("lead", "gggd", "loss", "")), 0)

    def test_any_path_different_length(self):
        # Test the any path creator function with normal start and target word that are not the same length
        self.assertEqual(len(main_for_test("lead", "gin", "", " ")), 0)
        self.assertEqual(len(main_for_test("lead", "gin", "tin", " ")), 0)
        self.assertEqual(len(main_for_test("lead", "gin", "lean", " ")), 0)

    def test_any_numbers(self):
        # Test the any path creator function with numbers
        self.assertEqual(len(main_for_test("45", "55", "", "8")), 0)
        self.assertEqual(len(main_for_test("45", "55", "55", "f")), 0)
        self.assertEqual(len(main_for_test("45", "55", "45", "g")), 0)

    def test_any_float_numbers(self):
        # Test the any path creator function with float numbers
        self.assertEqual(len(main_for_test("45.05", "55.03", "", "n")), 0)
        self.assertEqual(len(main_for_test("45.0566", "55.0566", "55", "66")), 0)
        self.assertEqual(len(main_for_test("45.000", "55.999", "45", "890.00")), 0)
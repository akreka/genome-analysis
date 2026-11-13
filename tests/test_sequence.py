
import unittest

from src.sequence import validate_sequence


class TestValidateSequence(unittest.TestCase):

    def test_valid_sequence(self):
        self.assertTrue(validate_sequence("ATGC"))

    def test_lowercase_sequence(self):
        self.assertTrue(validate_sequence("atgc"))

    def test_invalid_character(self):
        self.assertFalse(validate_sequence("ATGX"))

    def test_empty_sequence(self):
        self.assertFalse(validate_sequence(""))

    def test_sequence_with_numbers(self):
        self.assertFalse(validate_sequence("ATG123"))


if __name__ == "__main__":
    unittest.main()

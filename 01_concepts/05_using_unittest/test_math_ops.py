import unittest

from math_ops import Calculator  # if your are testing in same file do not import it


class TestCalculator(unittest.TestCase):

    # run once before EACH test method
    def setUp(self):
        self.calc = Calculator()
        print("\nSetting up resources...")

    # run once after EACH test method
    def tearDown(self):
        print("Cleaning up resources...")

    # Test names MUST start with 'test_'
    def test_add(self):
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_add_negative(self):
        result = self.calc.add(-1, -1)
        self.assertEqual(result, -2)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        # We expect a ValueError here using a context manager
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()

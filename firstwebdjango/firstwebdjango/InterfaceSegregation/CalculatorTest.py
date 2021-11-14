import unittest
from parameterized import parameterized

from firstwebdjango.InterfaceSegregation.BasicCalculator import BasicCalculator


class BasicCalculatorTest(unittest.TestCase):
    def test_CreateBasicCalculator(self):
        cal = BasicCalculator()

    def test_basic_calculator_add_two_numbers(self):
        cal = BasicCalculator()
        res = cal.Add(1, 2)
        self.assertEqual(3, res)

    def test_basic_calculator_sub_two_numbers(self):
        cal = BasicCalculator()
        res = cal.Sub(1, 2)
        self.assertEqual(-1, res, "Sub is not working")


class MyTestCase(unittest.TestCase):
    def test_basic_calculator_add_positive_numbers(self):
        cal = BasicCalculator()
        res = cal.Add(2, 3)

        self.assertEqual(5, res)  # add assertion here

    def test_basic_calculator_add_negative_numbers(self):
        cal = BasicCalculator()
        res = cal.Add(-2, -3)

        self.assertEqual(-5, res)  # add assertion here

    @parameterized.expand([
        ["test1", 2, 3, 5],
        ["test2", -2, -3, -5],
        ["test3", 5, -5, 0],
    ])
    def test_basic_calculator_add_numbers(self, name, a, b, expectedResult):
        cal = BasicCalculator()
        res = cal.Add(a, b)

        self.assertEqual(expectedResult, res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
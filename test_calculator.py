import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 5), 6)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(add(-1, -3), -4)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(-5, -5), 0)

    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(5, -5), -25)
        self.assertEqual(mul(-1, 1), -1)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 3), 1)
        self.assertEqual(div(1, -1), -1)
        self.assertAlmostEqual(div(-10, 3), -0.3)


    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(10, 100), 0.5)
        self.assertAlmostEqual(logarithm(1, 2.718), 0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(10, 24), 26)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == '__main__':
    unittest.main()

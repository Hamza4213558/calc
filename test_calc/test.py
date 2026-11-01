import unittest

from Calc import calcadd

class TestCalc(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(calcadd(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(calcadd(-1, -2), -3)


if __name__ == '__main__':
    unittest.main() 
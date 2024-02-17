import unittest
from main import add, substract, divide, multiply


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEquals(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -2), -3)

    def test_substract(self):
        self.assertEqual(substract(10, 5), 5)
        self.assertEqual(substract(-1, 1), -2)
        self.assertEqual(substract(-1, -2), 1)

    def test_mult(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -2), 2)

    def test_divide(self):
        self.assertEqual(divide(5, 10), 1 / 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -2), 1 / 2)

        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()

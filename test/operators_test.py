import unittest


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        a = 7
        b = 1
        self.assertFalse(a == b)

    def test_notequal(self):
        a = 7
        b = 7
        self.assertFalse(a != b)

    def test_less(self):
        a = 7
        b = 3
        self.assertFalse(a < b)

    def test_greater(self):
        a = 2
        b = 18
        self.assertFalse(a > b)

    def test_greater_or_equal(self):
        a = 9
        b = 10
        self.assertFalse(a >= b)

    def test_less_or_equal(self):
        a = 13
        b = 8
        self.assertFalse(a <= b)


if __name__ == '__main__':
    unittest.main()

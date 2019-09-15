import unittest
from format import average_scores


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(76.33, average_scores.average(65.22, 76.33, 87.44))


if __name__ == '__main__':
    unittest.main()

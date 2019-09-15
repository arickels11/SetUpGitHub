import unittest
from format import average_scores


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(90, average_scores.average(85,90,95))


if __name__ == '__main__':
    unittest.main()

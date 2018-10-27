import unittest
import Lab3


class MainTest(unittest.TestCase):

    def test_algorithm(self):
        test_lists = [
            [(1, 2), (2, 4), (3, 5)],
            [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)],
            [(4, 5)],
            [(1, 4), (2, 5), (5, 6), (7, 8)]
        ]

        test_results = [4, 6, 0, 8]

        for i in range(test_lists.__len__()):
            self.assertEqual(Lab3.algorithm(test_lists[i]), test_results[i])

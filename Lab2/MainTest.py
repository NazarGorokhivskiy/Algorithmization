import unittest
import Main


class MainTest(unittest.TestCase):

    def test_algorithm(self):
        test_lists = [
            [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)],
            [(0, 1), (3, 5), (4, 8), (0, 12), (9, 10)],
            [(11, 12), (8, 9), (2, 3), (9, 12)],
            [(1, 3), (4, 6), (10, 12), (0, 9)]
        ]
        test_results = [
            [(0, 1), (3, 8), (9, 12)],
            [(0, 12)],
            [(2, 3), (8, 12)],
            [(0, 9), (10, 12)]
        ]

        for i in range(test_lists.__len__()):
            self.assertEqual(Main.gorokhivskiy_algorithm(test_lists[i]), test_results[i])

import unittest
import Popularity


class MainTest(unittest.TestCase):

    def test_algorithm(self):
        inputs_for_testing = [
            "NNN NNN NNN",
            "NYY YNY YYN",
            "NYNNN YNYNN NYNYN NNYNY NNNYN"
        ]

        expected_results = [0, 2, 4]

        for i in range(inputs_for_testing.__len__()):
            matrix = Popularity.parse_string(inputs_for_testing[i])
            result = Popularity.find_max_friends(matrix)
            self.assertEqual(result, expected_results[i])

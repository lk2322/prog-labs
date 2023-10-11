import unittest
from io import StringIO
from unittest.mock import patch

age_groups = [18, 30, 40]
input_data = ["John,25", "Alice,32", "Bob,19", "END"]
expected_output = ['31-40: Alice (32)', '19-30: John (25), Bob (19)']


class TestAgeGroupSorting(unittest.TestCase):

    @patch("builtins.input", side_effect=[" ".join(map(str, age_groups))] + input_data)
    @patch("sys.stdout", new_callable=StringIO)
    def test_age_group_sorting(self, mock_stdout, mock_input):
        import src.lab4.survey
        output = mock_stdout.getvalue().strip().split("\n")
        self.assertEqual(output, expected_output)

import unittest
from unittest.mock import patch
from io import StringIO
from src.lab4.survey import AgeGroupClassifier

class TestAgeGroupClassifier(unittest.TestCase):
    def setUp(self):
        self.age_groups = [18, 25, 35, 50]
        self.classifier = AgeGroupClassifier(self.age_groups)

    @patch("builtins.input", side_effect=["John,22", "Sara,40", "END"])
    def test_process_input(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.classifier.process_input("John", 22)
            self.classifier.process_input("Sara", 40)
            self.classifier.display_results()
            output = mock_stdout.getvalue().strip()

        expected_output = "36-50: Sara (40)\n19-25: John (22)"
        self.assertEqual(output, expected_output)

    def test_classify_age_group(self):
        self.assertEqual(self.classifier.classify_age_group(20), '19-25')
        self.assertEqual(self.classifier.classify_age_group(40), '36-50')

if __name__ == '__main__':
    unittest.main()

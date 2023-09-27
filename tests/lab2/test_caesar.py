import unittest

from src.lab2.caesar import decrypt_caesar, encrypt_caesar


class CaesarTestCase(unittest.TestCase):

    def test_decrypt(self):
        """
        Test decrypt_caesar function.

        Input: encrypted string
        Output: decrypted string
        """
        # Test uppercase letters
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")

        # Test lowercase letters
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")

        # Test digits and special characters
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")

        # Test empty string
        self.assertEqual(decrypt_caesar(""), "")

    def test_encrypt(self):
        """
        Test encrypt_caesar function.

        Input: plaintext string
        Output: encrypted string
        """
        # Test uppercase letters
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")

        # Test lowercase letters
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")

        # Test digits and special characters
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")

        # Test empty string
        self.assertEqual(encrypt_caesar(""), "")
from string import ascii_lowercase, ascii_uppercase
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    result = ''

    for i in range(len(plaintext)):
        if plaintext[i].isupper():
            letter_n = ascii_uppercase.index(plaintext[i])
            key_n = ascii_uppercase.index(keyword[i % len(keyword)])
            value = (letter_n + key_n) % len(ascii_uppercase)
            result += ascii_uppercase[value]
        elif plaintext[i].islower():
            letter_n = ascii_lowercase.index(plaintext[i])
            key_n = ascii_lowercase.index(keyword[i % len(keyword)])
            value = (letter_n + key_n) % len(ascii_lowercase)
            result += ascii_lowercase[value]
        else:
            result += plaintext[i]

    return result


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    result = ''

    for i in range(len(ciphertext)):
        if ciphertext[i].isupper():
            letter_n = ascii_uppercase.index(ciphertext[i])
            key_n = ascii_uppercase.index(keyword[i % len(keyword)])
            value = (letter_n - key_n) % len(ascii_uppercase)
            result += ascii_uppercase[value]
        elif ciphertext[i].islower():
            letter_n = ascii_lowercase.index(ciphertext[i])
            key_n = ascii_lowercase.index(keyword[i % len(keyword)])
            value = (letter_n - key_n) % len(ascii_lowercase)
            result += ascii_lowercase[value]
        else:
            result += ciphertext[i]

    return result
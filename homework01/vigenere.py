def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for index, elem in enumerate(plaintext):
        if ord('A') <= ord(elem) <= ord('Z') or ord('a') <= ord(elem) <= ord('z'):
            extra = index % len(keyword)
            if ord('A') <= ord(elem) <= ord('Z'):
                change = ord(keyword[extra]) - 65
            if ord('a') <= ord(elem) <= ord('z'):
                change = ord(keyword[extra]) - 97
            pos = ord(elem) + change
            if pos > 90 and ord('A') <= ord(elem) <= ord('Z') or pos > 122 and ord('a') <= ord(elem) <= ord('z'):
                pos = pos - 26
            ciphertext = ciphertext + chr(pos)
        else:
            ciphertext = ciphertext + elem
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    for index, elem in enumerate(ciphertext):
        if ord('A') <= ord(elem) <= ord('Z') or ord('a') <= ord(elem) <= ord('z'):
            extra = index % len(keyword)
            if ord('A') <= ord(elem) <= ord('Z'):
                change = ord(keyword[extra]) - 65
            if ord('a') <= ord(elem) <= ord('z'):
                change = ord(keyword[extra]) - 97
            pos = ord(elem) - change
            if pos < 65 and ord('A') <= ord(elem) <= ord('Z') or pos < 97 and ord('a') <= ord(elem) <= ord('z'):
                pos = pos + 26
            plaintext = plaintext + chr(pos)
        else:
            plaintext = plaintext + elem
    return plaintext



   

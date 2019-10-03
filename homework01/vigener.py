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
    # PUT YOUR CODE HERE
    
    ciphertext = ''
    
    plaintext = plaintext.upper()
    keyword = keyword.upper() 
    
    l = len(keyword)
    numkey = [ord(i) for i in keyword]
    plaintext_int = [ord(i) for i in plaintext]
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + numkey[i % l]) % 26
        ciphertext = ciphertext + chr(value + 65)
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
    # PUT YOUR CODE HERE
    
    plaintext = ''

    ciphertext = ciphertext.upper()
    keyword = keyword.upper()

    l = len(keyword)
    numkey = [ord(i) for i in keyword]
    ciphertext_int = [ord(i) for i in ciphertext]
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - numkey[i % l]) % 26
        plaintext += chr(value + 65)
    return plaintext

print (decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
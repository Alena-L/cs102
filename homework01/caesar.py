def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    ciphertext = ''
    
    for elem in plaintext:
        if ('a' <= elem <= 'z') or ('A' <= elem <= 'Z'):
        ciph = ord(elem) + 3
            if ciph > (ord('Z') and ciph < ord('a')) or (ciph > ord('z')):
            ciph = ciph - 26
        ciphertext = ciphertext + chr(ciph)
        else:
        ciphertext = elem
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    return plaintext
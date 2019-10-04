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
    cipher = 0 
    
    for elem in plaintext:
        if (ord('a') <= ord(elem) <= ord('z')) or (ord('A') <= ord(elem) <= ord('Z')):
            cipher = ord(elem) + 3
            if (cipher > ord('Z') and cipher < ord('a')) or (cipher > ord('z')):  
               cipher = cipher - 26
            ciphertext = ciphertext + chr(cipher)
        else:
            ciphertext = ciphertext + elem
    return ciphertext

def decrypt_caesar(ciphertext):
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
    plaintext = ''
    ciph = 0

    for elem in ciphertext:
        if (ord('a') <= ord(elem) <= ord('z')) or (ord('A') <= ord(elem) <= ord('Z')):
            cipher = ord(elem) - 3
            if (cipher > ord('Z') and cipher < ord('a')) or (cipher < ord('A')):  
               cipher = cipher + 26
            plaintext = plaintext + chr(cipher)
        else:
            plaintext = plaintext + elem
    return plaintext

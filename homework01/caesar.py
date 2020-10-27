import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    #
    # CODE

    #plaintext = input()
    #shift = input()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in plaintext:
        if i.lower() in alphabet:
            if i in alphabet:
                ciphertext = ciphertext + alphabet[(alphabet.find(i) + int(shift)) % len(alphabet)]
            else:
                ciphertext = ciphertext + alphabet[(alphabet.find(i.lower()) + int(shift)) % len(alphabet)].upper()
        else:
            ciphertext = ciphertext + str(i)

    #print(ciphertext)

    # THE END CODE
    #

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    #
    # CODE

    #ciphertext = input()
    #shift = input()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in ciphertext:
        if i.lower() in alphabet:
            if i in alphabet:
                plaintext = plaintext + alphabet[(alphabet.find(i) - int(shift)) % len(alphabet)]
            else:
                plaintext = plaintext + alphabet[(alphabet.find(i.lower()) - int(shift)) % len(alphabet)].upper()
        else:
            plaintext = plaintext + str(i)

    #print(plaintext)

    # THE END CODE
    #

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift

#
# TESTING

#encrypt_caesar()
#decrypt_caesar()

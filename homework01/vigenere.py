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
    ciphertext = ""

    #
    # CODE

    #plaintext = input()
    #keyword = input()

    oldkeyword = keyword
    keyword = ''

    for i in range(len(plaintext)):
        keyword = keyword + oldkeyword[i % len(oldkeyword)]

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    q = 0

    for i in plaintext:
        x = keyword[q]
        q = q + 1
        if i.lower() in alphabet:
            if i.islower():
                ciphertext = ciphertext + alphabet[(alphabet.find(i.lower()) + alphabet.find(x.lower())) % len(alphabet)]
            else:
                ciphertext = ciphertext + alphabet[(alphabet.find(i.lower()) + alphabet.find(x.lower())) % len(alphabet)].upper()
        else:
            ciphertext = ciphertext + str(i)

    #print(ciphertext)

    # THE END CODE
    #

    return ciphertext


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
    plaintext = ""

    #
    # CODE

    #plaintext = input()
    #keyword = input()

    oldkeyword = keyword
    keyword = ''

    for i in range(len(ciphertext)):
        keyword = keyword + oldkeyword[i % len(oldkeyword)]

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    q = 0

    for i in ciphertext:
        x = keyword[q]
        q = q + 1
        if i.lower() in alphabet:
            if i.islower():
                plaintext = plaintext + alphabet[(alphabet.find(i.lower()) - alphabet.find(x.lower())) % len(alphabet)]
            else:
                plaintext = plaintext + alphabet[(alphabet.find(i.lower()) - alphabet.find(x.lower())) % len(alphabet)].upper()
        else:
            plaintext = plaintext + str(i)

    #print(plaintext)

    # THE END CODE
    #

    return plaintext

#
# TESTING

#decrypt_vigenere()
#decrypt_vigenere()

"""
File: caesar.py
Name: Quill
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    User will input a number to produce shifted ALPHABET as the cipher table,
    and any string typed in will be encrypted.
    """
    n = int(input('Secret number: '))
    s = str(input('What\'s the ciphered string? '))
    print('The deciphered string is: ' + deciphered(s, n))


def deciphered(s, n):
    """
    :param n: int, the secret number.
    :param s: str, a string is encrypted by caesar cipher.
    :return: deciphers the given string using the caesar cipher.
    """
    ans = ''
    s = s.upper()
    for i in range(len(s)):
        ch = s[i]
        for j in range(len(ALPHABET)):
            if ch == ALPHABET[j]:
                new_alphabet = (j + n) % len(ALPHABET)
                ans += ALPHABET[new_alphabet]
                break   # exit the inner loop once a match is found
        if not ch.isalpha():
            ans += ch    # keep the original string
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

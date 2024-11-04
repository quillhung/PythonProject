"""
File: complement.py
Name: Quill
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
The program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    Finding the complement strand of a DNA sequence.
    """
    dna = 'ATGC'
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: str, dna sequence.
    :return: str, complement strand of a dna sequence.
    """
    ans = ''
    for i in range(len(dna)):
        ch = dna[i]
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'G':
            ans += 'C'
        elif ch == 'C':
            ans += 'G'
    if ans == '':
        print('DNA strand is missing.', end='')
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

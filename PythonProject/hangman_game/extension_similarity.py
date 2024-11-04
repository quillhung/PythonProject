"""
File: similarity.py (extension)
Name: Quill
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    It will compare short dna sequence, s2,
    with subsequences of a long dna sequence, s1.
    """
    s1 = input('Please give me a DNA sequence to search: ').upper()
    s2 = input('What DNA sequence would you like to match? ').upper()
    print('The best match is ' + best_match(s1, s2))


def best_match(s1, s2):
    """
    param s1: long dna sequence
    param s2: short dna sequence
    return: the most similar dna subsequence in s1 to s2
    """
    ans = ''
    best_score = 0  # set the best score start with 0
    for i in range(len(s1) - len(s2) + 1):  # check each subsequence in s1 with the same length as s2
        ch = s1[i:i + len(s2)]
        score = 0
        for j in range(len(s2)):
            if ch[j] == s2[j]:
                score += 1  # if ch match in s2 get 1 score
        if score > best_score:
            best_score = score  # The subsequence with the highest scores is the most similar
            ans = ch
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

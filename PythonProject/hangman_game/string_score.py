"""
File: string_score.py
Name: Quill
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    This program calculates a score for a given string based on
    the types of characters it contains.
    """
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    """
    :param string: str.
    :return: int, a score for the string.
    """
    ans = 0
    for i in range(len(string)):
        ch = string[i]
        if ch.isdigit():
            ans += 1
    for i in range(len(string)):
        ch = string[i]
        if ch.isupper():
            ans += 2
    for i in range(len(string)):
        ch = string[i]
        if ch.islower():
            ans += 3
    print(ans)
    return ans


if __name__ == '__main__':
    main()

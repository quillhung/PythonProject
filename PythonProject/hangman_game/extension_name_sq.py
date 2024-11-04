"""
File: name_sq.py (extension)
Name: Quill
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    The square pattern of the given name will be printed on the console.
    """
    print('This program prints a name in a square pattern!')
    n = input('Name: ')
    square(n)
    reverse(n)


def square(n):
    """
    Print a normal n at first, then each line will gradually move the letters
    from the ends of n toward the center, and leaving spaces in the middle.
    """
    print(n)
    for i in range(1, len(n)-1):
        print(n[i], end='')
        print(' '*(len(n)-2), end='')
        print(n[-(i+1)])


def reverse(n):
    """
    reverse n string.
    """
    ans = ''
    for i in range(len(n)):
        ch = n[i]
        ans = ch + ans
    print(ans)
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

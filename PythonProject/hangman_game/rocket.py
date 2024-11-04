"""
File: rocket.py
Name: Quill
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This program that draws ASCII art - a rocket,
    and the size of rocket is determined by a constant defined as SIZE at top.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    Build head of the rocket.
    """
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def belt():
    """
    Build belt of the rocket.
    """
    for i in range(1):
        for j in range(1):
            print('+', end='')
        for j in range(SIZE*2):
            print('=', end='')
        for j in range(1, SIZE*2, SIZE*2+1):
            print('+', end='')
        print('')


def upper():
    """
    Build upper of the rocket.
    """
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(i+1):
            print('/', end='')
            print('\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


def lower():
    """
    Build lower of the rocket.
    """
    for i in range(SIZE):
        for j in range(1):
            print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\\', end='')
            print('/', end='')
        for j in range(i):
            print('.', end='')
        for j in range(1):
            print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

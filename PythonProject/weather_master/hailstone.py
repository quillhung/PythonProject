"""
File: hailstone.py
Name: Quill
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Implement a console program that simulates the execution
    of the Hailstone sequence, and count how many steps it takes.
    """
    print('This program computes Hailstone sequences.')
    print()
    n = int(input('Enter a number: '))
    step = 0
    while n != 1:
        if n % 2 == 0:
            print(str(n)+' is even, so I take half: '+str(n//2))
            n = n//2
        else:
            print(str(n)+' is odd, so I make 3n+1: '+str(n*3+1))
            n = n*3+1
        step += 1    # step = step+1. to count how many steps it takes.
    print('It took '+str(step)+' step to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

"""
File: hangman.py
Name: Quill
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    User putting one character each round, if the user input is correct, show the
    updated word on console. User have N_TURNS chances to try and win this game.
    """
    word = random_word()
    life = N_TURNS
    dashed = '-'*len(word)
    print('The word looks like: ' + dashed)
    print('You have ' + str(life) + ' wrong guesses left.')
    while life > 0:
        ch = input(str('Your guess: ')).upper()
        if not ch.isalpha() or len(ch) != 1:
            print('illegal format.')
        else:
            ans = ''
            if ch in word:
                for i in range(len(word)):
                    if ch == word[i]:
                        ans += ch
                    else:
                        ans += dashed[i]
                dashed = ans
                print('You are correct!')
            else:
                life -= 1
                print('There is no ' + ch + '\'s in the word.')
            if dashed == word:
                print('You win!!')
                print('The answer is: ' + word)
                break   # when user guesses the word, exit loop.
            if life > 0:
                # do not print 'you have 0 wrong guesses left.' when failed.
                print('The word looks like: ' + dashed)
                print('You have ' + str(life) + ' wrong guesses left.')
            if life == 0:
                print('You are completely hung :(')
                print('The answer is: ' + word)
    return


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

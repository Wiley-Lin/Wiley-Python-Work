"""
File: hangman.py
Name: Wiley Lin
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
Skills used in this file: string manipulation, function, if statement, while loop.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This function creates a game named Hangman, giving the player (N_TURNS) try.
    If the input is not alphabet or is more than two letters, it will show illegal format.
    """
    times = N_TURNS
    n = random_word()
    print('The word looks like: ' + whole(n))
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    ans = ''
    while True:
        guess = input('Your guess : ')
        capital = guess.upper()
        if len(capital) != 1:
            print('Illegal format.')
        else:
            if not capital.isalpha():
                print('Illegal format.')
            else:
                ans = ans + capital
                ch = show(n, ans)
                if capital in n:
                    if ch != n:
                        times = times - 0
                        print('You are correct!')
                        print('The word looks like: ' + str(ch))
                        print('You have ' + str(times) + ' wrong guesses left.')
                    else:
                        print('You win!!')
                        print('The answer is: ' + str(n))
                        break
                if capital not in n:
                    if times > 1:
                        times = times - 1
                        print('There is no ' + capital + "'s" + ' in the word.')
                        print('The word looks like: ' + str(ch))
                        print('You have ' + str(times) + ' wrong guesses left.')
                    else:
                        print('There is no ' + capital + "'s" + ' in the word.')
                        print('You are completely hung :(')
                        print('The answer is: ' + str(n))
                        break


def show(s, j):
    """
    This function shows the accumulated hints by using the collected inputs,
    it tells whether the collected inputs are in the original word, and shows the hints.
    """
    ans = ""
    for i in range(len(s)):
        alphabet = s[i]
        if s[i] in j:
            ans = ans + alphabet
        else:
            ans = ans + '-'
    return ans


def whole(r):
    """
    This function blocks the whole letter in the original word,
    specifically used for the first round.
    """
    ans = ""
    for i in range(len(r)):
        ch = r[i]
        ans = ans + '-'
    return ans


def random_word():
    """
    This function gives a random word from 9 options.
    """
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

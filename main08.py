#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')
    
#Before running
'''Line 9 allows the user to keep guessing what the computers favorite
color is over and over again instead of having to restart the program
over and over again. Lines 10 - 17 are indentied because they will only
be asked while you are wrong by NOT having typed in red.'''

#After running
''' If line 10 was moved up then if you immeditly guessed red no of the
program inside the while statement would run because it only runs while
you have not guessed red. Also if you guessed incorrectly then you would
get stuck inside the while loop with the same response repeating because
you wouldn't be allowed to input another guess.'''
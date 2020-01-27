#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#Before running
'''This program differs from the last one by adding a correct answer
to the question by using and if/else statement and it also gets rid of
the random print(color) statement. Lines 9 - 12 are seeing if you
guessed correctly. Lines 10 and 12 are indented because it shows what
path the indented code is a part of.'''

#After running
'''If you don't capatilize the word/color red the program will think
your wrong because it does not know that red is ment to equal Red.'''
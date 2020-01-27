#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red' or color == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#Before running
'''This program is diffent from the last because it allows the user
to enter Red or red and still be correct instead of just Red. It is
trying to solve the problem of people putting in the right color
but still getting the wrong answer by making it so any logical/normal
way of typing red will work.'''

#After running
'''If you type red in a odd way like ReD or REd the program will think
your wrong, because as I said, it is designed to make any NORMAL/LOGICAL
way of typing red correct, not odd/dumb ways.'''
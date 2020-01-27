#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#Before running
'''Line 9 will now turn any word, no matter how it is
capatilized, to all just lower case letters and then check if it is red.
This is trying to solve the problem of having a strict naming set so
it is more easy to use, makes more sense, and stops people from being
both right and wrong.'''

#After running
''' if you add spaces before, in, or after red the program will lable
your answer as wrong because it is not designed to take those spaces
into consideration.'''

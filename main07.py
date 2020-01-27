#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
color = color.lower().strip()
if (color == 'red'):
    print('Correct!')
elif (color == 'pink'):
    print('Close!')
else:
    print('Sorry, try again.')

#Before running
'''This program is diffrent from the last because it has made the color
you type in fix its self before the if/else statement. It also added
a third pathway, if you type a form of pink (without something added on)
, you will get "Close!" instead of you just being flat out wrong. On
line 12 it is giving you that third path way of pink.'''

#After running
'''No comment required.'''
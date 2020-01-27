#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
count = 0
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    count = count + 1               # You can also write this as count += 1
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')

print('You guessed it in {} tries!'.format(count))

#Before running
''' On line 13 a running total of how many guesses you've taken is set
up. Count allows the program to see how many times the user has tried
because everytime they try to guess count will go up by one. Line 22
is empty but on line 21 the program is coming to an end by telling you
how many times you guessed.'''

#After running
'''No comment required.'''
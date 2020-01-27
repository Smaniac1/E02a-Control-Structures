#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#Before running
'''This program is diffrent from the last because in line 9 it also
adds the .strip() command to what you typed in. This should just get
rid of any spaces so that if you type in red in any way with spaces
(that are NOT inside the word red) or capatilized letters it will 
still work.'''

#After running
'''You can still break the logic by adding something else like
red. instead of just red like normal or putting spaces inside 
the word.'''
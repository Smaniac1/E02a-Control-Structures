#!/usr/bin/env python3

#The program imports needed types of commands
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

#The program greats the user
print('Greetings!') 
#The program sets up a list of colors for later
colors = ['red','orange','yellow','green','blue','violet','purple']
#The program sets up a way for the user to say if they want to continue or not
play_again = ''
#sets up a way for the user to track their best count
best_count = sys.maxsize            # the biggest number

#Sets up a while loop that will only end if the user wants it to
while (play_again != 'n' and play_again != 'no'):
    #The program chooses a random color from 'colors'
    match_color = random.choice(colors)
    #The program sets up the counter for the one game (not the best overall)
    count = 0
    #The program sets up the variable to put the users guesses in
    color = ''
    #Sets up a while loop that only end when the user has guessed the right color
    while (color != match_color):
        #The program has the user put in their guess
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        #The program formats the users input to make the amount of correct answers more broad
        color = color.lower().strip()
        #makes the count go up each time the user puts in a guess
        count += 1
        #sets up the correct pathway that ends the game
        if (color == match_color):
            #The message the user gets when they guessed right
            print('Correct!')
        #Sets up the pathway the user goes down if they get it wrong
        else:
            #The message the user gets when they got it wrong and have to guess again
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    #The message the user gets when the program ends after they got it right
    print('\nYou guessed it in {} tries!'.format(count))

    #Sets up the recording of the users best count, they only go down this is if this is their best game yet
    if (count < best_count):
        #Tell the user that this was their best game
        print('This was your best guess so far!')
        #Has the program record their new best count
        best_count = count

    #Asks the user if they want to play the game again or quit
    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

#The message the user gets when they have told the program they do not want to play again
print('Thanks for playing!')
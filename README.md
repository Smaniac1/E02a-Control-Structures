
Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
  - What do you think the program did with what you typed in answer to the question?
- Open main02.py. Before running it, describe how this is different than main01.py.
  - What do you think the color = input() will do?
  - Run the program in the terminal and answer the question. Did the program do what you expected?
- Open main03.py. Before running it, describe how this is different than main02.py.
  - What is happening on lines 9–12?
  - Why are lines 10 and 12 indented?
  - Run the program and answer the question. What happens if you don’t capitalize Red?
  - What does this tell you about "color"?
- Open main04.py. Before running it, describe how this is different than main03.py.
  - What problem is this trying to solve?
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
- Open main05.py. What do you expect line 9 to do?
  - What problem is it trying to solve?
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
 - Open main06.py. How is line 9 different than in main05.py?
   - What would you guess .strip() is doing?
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
   - What is happening on line 12?
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
   - Why are lines 10–17 indented?
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
 - Open main09.py. What is happening on line 13?
   - What is the purpose of “count”?
   - What is happening on line 22?
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
  
Commit your changes and push them back to the repository.
 
 main01.py

 #Before running
'''I think the program will say "Greetings!" followed by asking my
what 'its' favorite color is. After I put that in the program will
end as there is no more code.'''

#After running
''' The program did exactly what I said it would do above. I know the
program took my guess but I don't think it stored it as the 
input has no variable connected to it, so it probably immediately
deleted it afterwards.'''

main02.py

#Before running
''' This program is different from the last in two ways. First off
it actually stores my guess into a varible (color), but 
then it also prints out what I guessed back out. I think the
color = input() will actually store what I type in unlike the last one
were it didn't have a variable to store it in.'''

#After running
'''The program did what I thought it was going to do, no suprises'''

main03.py

#Before running
'''This program differs from the last one by adding a correct answer
to the question by using and if/else statement and it also gets rid of
the random print(color) statement. Lines 9 - 12 are seeing if you
guessed correctly. Lines 10 and 12 are indented because it shows what
path the indented code is a part of.'''

#After running
'''If you don't capatilize the word/color red the program will think
your wrong because it does not know that red is ment to equal Red.'''

main04.py

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

main05.py

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

main06.py

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

main07.py

#Before running
'''This program is diffrent from the last because it has made the color
you type in fix its self before the if/else statement. It also added
a third pathway, if you type a form of pink (without something added on)
, you will get "Close!" instead of you just being flat out wrong. On
line 12 it is giving you that third path way of pink.'''

#After running
'''No comment required.'''

main08.py

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

main09.py

#Before running
''' On line 13 a running total of how many guesses you've taken is set
up. Count allows the program to see how many times the user has tried
because everytime they try to guess count will go up by one. Line 22
is empty but on line 21 the program is coming to an end by telling you
how many times you guessed.'''

#After running
'''No comment required.'''
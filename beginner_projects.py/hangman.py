#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

import random


word_list = ["deepan", "gokul", "santhosh","ajay","abinesh","rishikesh","dhinesh"]
chosen = random.choice(word_list)

chosenlen = len(chosen)

end_of_game = True
lives = 7



#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

import hangman_art
from hangman_art import logo

print(logo)

#Testing code

print(f'Pssst, the solution is {chosen}.')


#Create blanks
display = []
for d in range(chosenlen):
    display +="_"
    

while end_of_game:
    guess = input("guess the letter : ").lower()
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
            print("already found..")

    for position in range(chosenlen):
        letter = chosen[position]
        
        if letter == guess:
            display[position] = letter
           

    if guess  not in chosen:
        print("you found a  wrong letter.")
        
        lives-=1
        if lives == 1:
            end_of_game = False
            print("you lose ! !..")
            print("""
_____________________
!!!...GAME OVER...!!!
______________________""" )



    print(f" ".join(display))

      

    if '_' not in display:
        end_of_game = True
        print("you win !!..")

        #TODO-2: - Import the stages from hangman_art.py and make this error go away.


    from hangman_art import stages
    print(stages[-lives])

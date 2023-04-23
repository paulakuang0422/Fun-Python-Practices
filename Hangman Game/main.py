#import all the module you need
import random as rd
import hangman_words as hw
import hangman_art as ha
import replit as rp

# set up the initial parameters
chosen_word = rd.choice(hw.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []
glist=[]

#game header decor and wordings.
print(ha.logo)
print(f'Pssst, the solution is {chosen_word}.')

#create a list with all "_" in display
for _ in range(word_length):
    display += "_"

#while loop for each guessing
while not end_of_game:
    #ask user to guess
    guess = input("Guess a letter: ").lower()
    rp.clear()
    
    #check if user enter repeated letter
    if guess in glist:
        print(f" this lette {guess} has been used")
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.and result show is wrong
    if guess not in chosen_word:
        print(f"this letter {guess} not in the chosen word")
        lives -= 1
        #check if user used all lives
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    glist.append(guess)

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #print the hangman graph for each guessing
    print(ha.stages[lives])
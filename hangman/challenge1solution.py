
#Step 1 

word_list = [ "Andhra Pradesh",
                "Arunachal Pradesh",
                "Assam",
                "Bihar",
                "Chhattisgarh",
                "Goa",
                "Gujarat"
               ]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

#Step 1 


#TODO-1 - Randomly choose a word from the word_list ,convert to lowercase and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list).lower()
#Testing code
print(f'the solution is {chosen_word}.')
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("guess the letter").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")





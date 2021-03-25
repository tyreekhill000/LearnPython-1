import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list= ['camel','horse','ox']
#Randomly choose a word from wordlist
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for num in range(0,len(chosen_word)):
    display.append("-")
print(display)
#ask the user to guess the letter
#check if the letter user guessed is available
while "-" in display:
    guessingletter=input("Choose a letter").lower()
    for leter in range(0,len(chosen_word)):
        if chosen_word[leter]==guessingletter:
            display[leter]=guessingletter
        else:
            print(stages[-1]);
            stages.pop()
            break;
           
    if (len(stages)==0):
         print("You loose")
    print(display)

if "-" not in display:
    print("You win")
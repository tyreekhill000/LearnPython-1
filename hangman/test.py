import random
from hangman_words import word_list
from hangman_art import logo,stages
#Generate a random word
chosen_word=random.choice(word_list)
chosen_word_length=len(chosen_word)
print (logo)
print("testing ==" + chosen_word)
dispaly=[]

# generate as many blanks as in the chosen word
for count in range(chosen_word_length):
      dispaly.append("_")  

#join each element in the  dispaly with empty space string 
join_string=" "   
dispaly_string=join_string.join(dispaly)
print(dispaly_string)

game_can_continue=True
lives=len(stages) -1

while game_can_continue:
      #ask the user to guess the letter
      guess=input("Guess a letter  : ")

      # inform the user if the letter is already available in the display list
      if guess in dispaly:
            print("Guess another letter")
            
      # check if the guesses letter in the word
      for position in range(chosen_word_length):
            letter=chosen_word[position]
            if letter==guess:
                  dispaly[position]=letter
            
      # check if the guessed letter is not in the chosen_word .
      if guess not in chosen_word:
            print(f"your guess  {guess} is wrong. you loose a life")
            print(stages[lives])
            if lives==0:
                  print("You loose")
                  game_can_continue=False
            #loose a life
            lives-=1
            
            
                  
      #check if no blank "_" is available in the display list
      if "_"  not in dispaly:
            print("You win")
            game_can_continue=False
       
      dispaly_string=join_string.join(dispaly)
      print(dispaly_string)
      
      
      
      
      
 






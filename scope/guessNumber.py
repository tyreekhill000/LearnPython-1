import random 
from logo import art
print (art)
print("Welcome to the Number Guessing Game!")
print ("I'm thinking of a number between 1 and 100.")
number=random.randrange(1,100)
print(f"The number is  {number}")
difficulty_type=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_type =='easy':
  chances_left=10
else:
 chances_left=5
guessed_number=0
while guessed_number!=number:
  print (f"You have {chances_left} attempts remaining to guess the number")
  guessed_number=int (input("guess the number \n"))
  if (guessed_number >number ):
    print("Too high ")
    print("Guess again.")
    chances_left-=1
  
  elif (guessed_number< number ):
    print("Too Low ")
    print("Guess again.")
    chances_left-=1
  else:
     print("you guessed it correct")
  if (chances_left ==0):
    print("You ran out of chances")
    exit()
    



   


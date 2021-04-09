import random
from replit import clear
from art import logo

to_play=True
to_loop=True


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  sum_of_cards=sum(cards)
  if (sum_of_cards==21 ):
    return 0
  else:
    return sum_of_cards

def checkandModiify(lastcard,card_list):
  sum_of_the_cards=calculate_score(card_list)
  if (lastcard==11 and sum_of_the_cards>21):
        card_list.remove(lastcard)
        card_list.append(1)
  return card_list
  
def prepare_initial_two_cards(user_cards,computer_cards):
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def play_game():
  print(logo)
  user_cards=[]
  computer_cards=[]  
  to_loop=True
  prepare_initial_two_cards(user_cards,computer_cards)
  user_score=calculate_score(user_cards)
  computer_score=calculate_score(computer_cards)
  print(f"sum_user_cards {user_cards}")
  print(f"sum_user_cards {user_score}")
  print(f" first card of computer =={computer_cards[0]}")
  
  if(user_score==0):
    print("BlackJack You win")   
    to_loop=False  
  
  if(computer_score==0 ):
     print(" BlackJack for computer You loose")
     to_loop=False 
  if(user_score >21):
     print("Sum is greater than 21 at the start itslef")
     user_cards=checkandModiify(0,user_cards)
  if(computer_score >21 ):
     print("Sum is greater than 21 at the start itslef")
     computer_cards=checkandModiify(0,computer_cards)
  

  while to_loop: 
    to_continue=input ("Do you wish to take another card ? type yes or no")
    if(to_continue=="yes"):
      card=deal_card()
      user_cards.append(card)
      if(card==11):
       user_cards=checkandModiify(card,user_cards)
      user_score=calculate_score(user_cards)
      print(f"user_cards {user_cards}")
      print(f"sum_user_cards {user_score}")
      print(f" first card of computer =={computer_cards[0]}")
      if (user_score ==0):
        print("BlackJack for You u win")
        to_loop=False
    
      elif (user_score >21):
        print("you Loose because sum_user_cards >21 ")
        to_loop=False
    
    else: 
          computer_score=calculate_score(computer_cards)
          if(computer_score>17):
            if (computer_score >user_score):
               print("Computer win")
               to_loop=False
            else:
              print("You win")
              to_loop=False 
          else:
           while(computer_score!=0 and computer_score<17):
            card=deal_card()
            computer_cards.append(card)
            computer_cards=checkandModiify(card,computer_cards)
            computer_score=calculate_score(computer_cards)            
            if (computer_score ==0 ):
               print("BlackJack for Coputer u loose")
               to_loop=False 
            elif(computer_score >21):
              print("you win") 
              to_loop=False
            
            elif(computer_score == 21):
              print(f"you loose as computer toltal is {computer_score}")
              to_loop=False
          
          if (computer_score >user_score and computer_score <=21):
              print("Through sum_computer_cards >sum_user_cards and sum_computer_cards <=21")
              print("computer win") 
              to_loop=False
          elif(computer_score==user_score):
            print("Math draw")  
            to_loop=False
          elif(computer_score==17 and computer_score<user_score):
            print("when sum_computer_cards=17") 
            print("You win")
            to_loop=False   
  print(f"computer_cards {computer_cards}")
  print(f"user_cards {user_cards}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
         
        


      


      

    




    


 
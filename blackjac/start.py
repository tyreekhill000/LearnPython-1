import random
from replit import clear

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

def continue_play():
  return input ("Do you want to play a new game again ? type yes or no")

  
def prepare_initial_two_cards(user_cards,computer_cards):
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

 

def play_game():
  user_cards=[]
  computer_cards=[]  
  to_loop=True
  prepare_initial_two_cards(user_cards,computer_cards)
  sum_user_cards=calculate_score(user_cards)
  sum_computer_cards=calculate_score(computer_cards)
  print(f"sum_user_cards {user_cards}")
  print(f"sum_user_cards {sum_user_cards}")
  print(f" first card of computer =={computer_cards[0]}")
  #print(f"sum_computer_cards {sum_computer_cards}")
  
  if(sum_user_cards==0):
    print("BlackJack You win")   
    to_loop=False  
  
  if(sum_computer_cards==0 ):
     print(" BlackJack for computer You loose")
     to_loop=False 
  if(sum_user_cards >21):
     print("Sum is greater than 21 at the start itslef")
     user_cards=checkandModiify(0,user_cards)
  if(sum_computer_cards >21 ):
     print("Sum is greater than 21 at the start itslef")
     computer_cards=checkandModiify(0,computer_cards)
  

  while to_loop: 
    to_continue=input ("Do you wish to take another card ? type yes or no")
    if(to_continue=="yes"):
      card=deal_card()
      user_cards.append(card)
      if(card==11):
       user_cards=checkandModiify(card,user_cards)
      sum_user_cards=calculate_score(user_cards)
      print(f"user_cards {user_cards}")
      print(f"sum_user_cards {sum_user_cards}")
      if (sum_user_cards ==0):
        print("BlackJack for You u win")
        to_loop=False
        user_cards=[]
        computer_cards=[]  
    
      elif (sum_user_cards >21):
        print("you Loose because sum_user_cards >21 ")
        to_loop=False
    
    else: 
          sum_computer_cards=calculate_score(computer_cards)
          if(sum_computer_cards>17 and to_continue == "no"):
            if (sum_computer_cards >sum_user_cards):
               print("Computer win")
               to_loop=False
            else:
              print("You win")
              to_loop=False 
          else:
           while(sum_computer_cards!=0 and sum_computer_cards<17):
            card=deal_card()
            computer_cards.append(card)
            computer_cards=checkandModiify(card,computer_cards)
            sum_computer_cards=calculate_score(computer_cards)
            

            if (sum_computer_cards ==0 ):
               print("BlackJack for Coputer u loose")
               to_loop=False 

            elif(sum_computer_cards >21):
              print("you win") 
              to_loop=False
            
            elif(sum_computer_cards == 21):
              print(f"you loose as computer toltal is {sum_computer_cards}")
              to_loop=False
          
          if (sum_computer_cards >sum_user_cards and sum_computer_cards <=21):
              print("Through sum_computer_cards >sum_user_cards and sum_computer_cards <=21")
              print("computer win") 
              to_loop=False
          elif(sum_computer_cards==sum_user_cards):
            print("through compare") 
            print("Math draw")  
            to_loop=False
          elif(sum_computer_cards==17 and sum_computer_cards<sum_user_cards):
            print("when sum_computer_cards=17") 
            print("You win")
            to_loop=False   
    print(f"computer_cards {computer_cards}")
    print(f"sum_computer_cards {sum_computer_cards}")
    print(f"user_cards {user_cards}")
    print(f"sum_user_cards {sum_user_cards}") 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
         
        


      


      

    




    


 
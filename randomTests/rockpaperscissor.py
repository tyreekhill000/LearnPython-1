rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
print(rock)

# Paper
paper=''''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''


scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
print("Rules :Rock wins against scissors.\n Scissors win against paper.\n Paper wins against rock.\n")
types=[rock,paper,scissor]
user_chosen_index=int(input("Type 0 for Rock, 1 for Paper and 2 for scissors\n"))

if user_chosen_index >=3 or user_chosen_index < 0:
    print("You chose invalid number")
else:
    user_chosen_type=types[user_chosen_index]
    computer_chosen_index=random.randint(0,len(types)-1)
    #computer_chosen_type=types[computer_chosen_index]
    computer_chosen_type=random.choice(types)
    print(user_chosen_type)
    print(computer_chosen_type)

    if(user_chosen_type == rock and computer_chosen_type==scissor ):
        print("You win")
    elif(user_chosen_type == scissor and computer_chosen_type==paper ):
        print("You win")
    elif(user_chosen_type == paper and computer_chosen_type==rock ):
         print("You win")
    elif((user_chosen_type == paper and computer_chosen_type==paper) or (user_chosen_type == rock and                     computer_chosen_type==rock) or (user_chosen_type == scissor and computer_chosen_type==scissor) ):
         print("draw")
    else:
        print("computter wins")






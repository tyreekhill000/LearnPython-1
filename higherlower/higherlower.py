import random
from data import data
from art import vs,logo
from clear import clear
clear()
print(logo)

game_countinue_flag=True
def random_account():
    return random.choice(data)
def fromat_account(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name},{description} from {country}"

def check_answer(guess,follower_count_a,follower_count_b):
    if follower_count_a >follower_count_b:
        return guess =="a"
    else:
        return guess=="b"
account_b=random_account()
score=0
while game_countinue_flag :
    #Generate a random account from the game data.
    account_a=account_b
    account_b=random_account()
    while(account_a== account_b):
        account_b=random_account(data)



    # Format account data into printable format.
    print (f"Compare A : {fromat_account(account_a)}")
    print(vs)
    print (f"Against B : {fromat_account(account_b)}")
    # Ask user for a guess.
    guess=input ("Who has more followers? Type 'A' or 'B':").lower()
    ## Get follower count.
    follower_count_a=account_a["follower_count"]
    follower_count_b=account_b["follower_count"]
    # Check if user is correct.
    ## If Statement
    is_answer=check_answer(guess, follower_count_a,follower_count_b)

    # Feedback.
    # Score Keeping.
    clear()
    print(logo)
    if is_answer==True:
        score+=1
        print(f"You're right ! Current Score {score}")
    else:
        print(f"Sorry that's wrong.Final Score:{score}")
        game_countinue_flag=False

   


# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
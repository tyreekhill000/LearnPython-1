import random
import data
from art import logo, vs
from clear import clear
# Generate a random account from the game data.

def get_random_account():
      random_account=random.choice(data.data)
      return random_account
def format_data(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, a {description}, from {country}"
    
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
   

# Format account data into printable format.
print(logo)
score=0
game_should_continue=True
account_a=get_random_account()
account_b =get_random_account()

while game_should_continue:
    account_a = account_b
    account_b = get_random_account()
    while account_a ==account_b:
      account_b =get_random_account()
    print(f"Compare A {format_data(account_a)}")
    print(vs)
    print(f"against B {format_data(account_b)}")
    guess =input("Who has more followers. Type A or B").lower()
    a_follwers=account_a["follower_count"]
    b_follwers=account_b["follower_count"]
    is_correct=check_answer(guess,a_follwers,b_follwers)
    clear()
    print(logo)
    if(is_correct):
        score+=1
        print(f"You are correct and your score is {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")      
        game_should_continue=False
    
    
    



    
# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
# the variable name should always start with character, 
#when there are multiple words separate it with _ (user_name)
#Always create a meaninful variable name

user_name=input("What is your name?")
#number should not be used at the begining of the variable
length=len(user_name)
print(f"username is {user_name}")
print(f"length username is {length}")
# if you give the wrongvariable you will get syntax eror undefined_name user_nam and lengt
# print(f"username is {user_nam}") 
# print(f"length username is {lengt}")

#Quiz:
#Which line of Python code is valid?
# var a =12
# a =12
# a:12
# 12=a

#Which is the best variable name for Player 1's username?
# p1 user name ="Sachin"
# player1_user_name="Sachin"
# 1_player_username="Sachin"
# plu="Sachin"

#solution player1_user_name="Sachin"

#Which block of code will produce an error? For extra points, which type of error do you think it will produce?
# time_until_midnight="5"
# print("There are "+time_until_Midnight+ " until midnight")

# input="5"
# print("There are "+input+ " until midnight")

# time_until_midnight="5"
# print("There are "+time_until_midnight+ " until midnight")


#solution print("There are "+time_until_Midnight+ " until midnight") ->undefined_name time_until_Midnight
# There is a typo in the last line, it should be time_until_midnight not time_until_Midnight. Because when the name of the variable was used it was not spelt the same, you will get a name error.



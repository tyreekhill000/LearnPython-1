# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# 🚨 Don't change the code above 👆
amount=0
size_amount=0
pepperoni_amount=0
extra_cheese_amount=0

if (size=='S'):
  size_amount=15
elif size=='M':
  size_amount=20
elif size=='L':
  size_amount=25

if (add_pepperoni=='Y' and size=='S'):
  pepperoni_amount=2
elif (add_pepperoni=='Y' and (size=='M'or size=='L')):
  pepperoni_amount=3
else:
  pepperoni_amount=0

if (extra_cheese=='Y'):
  extra_cheese_amount=1
else:
  extra_cheese_amount=0

amount=size_amount+pepperoni_amount+extra_cheese_amount

print(amount)












#Write your code below this line 👇


# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
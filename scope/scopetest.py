################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#Local Scope -> exi
# def drink_potion():
#   potion_strength=2
#   print(potion_strength)

# drink_potion()
# print(potion_strength) # This code will not wrok as potion_strength is not with in scope . It is actually available in drink_potion 


#Global Scope
player_health=10 
def drink_potion():
  potion_strength=2
  print(player_health)

drink_potion()
print(player_health) # This code will not wrok as potion_strength is not with in scope . It is actually available in drink_potion 



  #nested function 
# player_health=10 
# def game():
#   def drink_potion():
#     potion_strength=2
#     print(player_health)
#   drink_potion()
#   print(player_health) # This code will not wrok as potion_strength is not with in scope . It is actually available in drink_potion 

#There is no block Scope:

enemies_level=3
enemies=['Skeleton','Zombies','Alien']
if enemies_level <5 :
  new_enemy=enemies[0]
print(new_enemy)

def create_enemy():
  enemies=['Skeleton','Zombies','Alien']
  if enemies_level <5 :
    new_enemy=enemies[1]

print(new_enemy)
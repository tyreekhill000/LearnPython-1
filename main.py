import random
print(random.uniform(10,100))
#fruits=input("Enter the fruit names followed by comma and space").split(", ")
#len(fruits)
fruits=["prav", "pra", "pr", "p"]
print(fruits[random.randint(0,len(fruits)-1)])
print(fruits)

#print(random.choice(fruits))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen[0][0])
emoji1=['😀','😀','😃']
emoji2=['😁','😆','😅']
emoji3=['😂','🤣','😇']
emoji=[emoji1,emoji2,emoji3]

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")
number= input("choose the number")
int_first_number=int(number[0])
int_second_number=int(number[1])
map[int_first_number-1][int_second_number-1]=emoji[int_first_number-1][int_second_number-1]
print(f"{map[0]}\n{map[1]}\n{map[2]}")

 




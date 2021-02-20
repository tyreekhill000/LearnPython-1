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
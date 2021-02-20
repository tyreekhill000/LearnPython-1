import random
print("Who will pay the restaurant Bill")
names=input("Enter the name seperated by , and space\n").split(", ") #split is a function that splits the string based on argument we pass
names_length=len[names]
bill_payer=names[random.randint(0,names_length-1)]
print(f"Bill will be paid by {bill_payer}")




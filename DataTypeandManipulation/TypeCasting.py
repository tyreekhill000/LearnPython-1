num_char=len(input("What is your name"))
print(type(num_char))
new_num_char=str(num_char)
print("After type casting")
print(type(new_num_char))
print("Your name has "+new_num_char+ " characters") # This will not break as the Type of new_num_char is String now 

#other 
#Guess what will print
print(100+float(100.75))
print(str(100)+str(100))
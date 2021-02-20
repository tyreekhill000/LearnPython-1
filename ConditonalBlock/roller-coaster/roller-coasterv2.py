# if condition:
#     if condition:
#       do some code
#     else:
#       do some code 
# else:
#     do some code 

print("Welcome to tthe roller coaster")
int_height=int(input("what is your height\n")) # converting Strig to int
int_age=int(input("What is your age\n"))
#Note the collon used after if conditon
if (int_height>120):  # checking if the height is greater than 120 cm
    print("You are allowed") # Note the Indentation 
    if(int_age >18):
        print("price == 10")
    else:
         print("price == 5")
else: #Note the collon used after if conditon
    print("You are not allowed")# Note the Indentation 
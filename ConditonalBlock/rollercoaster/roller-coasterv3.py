# if /elif/else

   # if condition:
#     if condition:
#       do some code
#    elif condition:
#       do some code
#    else:
#       do some code 
# else:
#     do some code 

print("Welcome to the roller coaster")
int_height=int(input("what is your height\n")) # converting Strint to int
#Note the collon used after if conditon
if (int_height>120):# checking if the height is greater than 120 cm
    print("You are  allowed") 
    int_age=int(input("What is your age\n"))
    if(int_age <12 ): #Note the collon used after if conditon .. Use Conditional operator >=
        print("price == 5")
    elif(int_age<=18): #Note the collon used after elif conditon .. Used Conditional operator >= and<
        print("price == 8")
    else:
         print("price == 10")
else: #Note the collon used after if conditon
    print("You are not allowed")# Note the Indentation
print("Welcome to the roller coaster")
int_height=int(input("what is your height\n")) # converting Strint to int
int_bill=0;
#Note the collon used after if conditon
if (int_height>120):  # checking if the height is greater than 120 cm
    print("You are allowed") # Note the Indentation 
    int_age=int(input("What is your age\n"))
    if(int_age <12 ): #Note the collon used after if conditon .. Use Conditional operator >=
        bill=5
    elif(int_age<=18): #Note the collon used after elif conditon .. Used Conditional operator >= and<
        bill=8
    else:
        bill=10
     
    
else: #Note the collon used after if conditon
    print("You are not allowed")# Note the Indentation
photo_required=input("Do you need Photo type Y or N")       
          
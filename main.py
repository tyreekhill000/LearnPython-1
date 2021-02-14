#if else
# if condition:
#     do some code
#  else:
#     do some code

# print("Welcome to tthe roller coaster")
# int_height=int(input("what is your height\n")) # converting Strint to int
# #Note the collon used after if conditon
# if (int_height>120):  # checking if the height is greater than 120 cm
#     print("You are allowed") # Note the Indentation 
# else: #Note the collon used after if conditon
#     print("You are not allowed")# Note the Indentation 

#Odd or even 
# print("Odd or Even")
# number=int(input ("Enter the number "))
# if(number%2==0):
#     print(f"{number} is even number")
# else:
#     print(f"{number} is odd number")

#nested if else

# if condition:
#     if condition:
#       do some code
#     else:
#       do some code 
# else:
#     do some code 

# print("Welcome to tthe roller coaster")
# int_height=int(input("what is your height\n")) # converting Strint to int
# int_age=int(input("What is your age\n"))
# #Note the collon used after if conditon
# if (int_height>120):  # checking if the height is greater than 120 cm
#     print("You are allowed") # Note the Indentation 
#     if(int_age >18):
#         print("price == 10")
#     else:
#          print("price == 5")
# else: #Note the collon used after if conditon
#     print("You are not allowed")# Note the Indentation 

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
int_age=int(input("What is your age\n"))
#Note the collon used after if conditon
if (int_height>120):  # checking if the height is greater than 120 cm
    print("You are allowed") # Note the Indentation 
    if(int_age <12 ): #Note the collon used after if conditon .. Use Conditional operator >=
        print("price == 5")
    elif(int_age<=18): #Note the collon used after elif conditon .. Used Conditional operator >= and<
        print("price == 8")
    else:
         print("price == 10")
else: #Note the collon used after if conditon
    print("You are not allowed")# Note the Indentation
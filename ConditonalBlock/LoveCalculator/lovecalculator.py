print("Welcome to Love caluclator")
your_name= input("What is your name")
partner_name= input ("What is your friend name")
lower_your_name=your_name.lower()
lower_partner_name=partner_name.lower()
combined_name=lower_your_name+lower_partner_name;
print(combined_name)

t_int=combined_name.count("t") 
r_int=combined_name.count("r")
u_int=combined_name.count("u")
e_int= combined_name.count("e")
sum_true=(t_int+r_int+u_int+e_int)


l_int=combined_name.count("l") 
o_int=combined_name.count("o")
v_int=combined_name.count("v")
e_int= combined_name.count("e")

sum_love=(l_int+o_int+v_int+e_int)

Love_score=str(sum_true)+str(sum_love)
 # Both number together
Love_score = int(f"{sum_true}{sum_love}")

if Love_score < 10 or Love_score > 90:

    print(f"Your score is {Love_score}, you go together like coke and mentos.")

elif Love_score > 40 and Love_score < 50:

    print(f"Your score is {Love_score}, you are alright together.")

else:

    print(f"Your love score is {Love_score}")


print("Welcome to Friendship caluclator")
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


f_int=combined_name.count("f") 
r_int=combined_name.count("r")
i_int=combined_name.count("i")
e_int= combined_name.count("e")
n_int= combined_name.count("n")
d_int= combined_name.count("d")

sum_friend=(f_int+r_int+i_int+e_int+n_int+d_int)

friend_score=str(sum_true)+str(sum_friend)
 # Both number together
friend_score = int(f"{sum_true}{sum_friend}")

if friend_score < 10 or friend_score > 90:

    print(f"Your score is {friend_score}, you go together like coke and mentos.")

elif friend_score > 40 and friend_score < 50:

    print(f"Your score is {friend_score}, you are alright together.")

else:

    print(f"Your Friendship score is {friend_score}")


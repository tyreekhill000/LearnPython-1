# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int=int(age)
remaining_age=90-age_as_int # assuming 90 years is the max age one can live
age_in_days=remaining_age*365 # remaining number of days
age_in_weeks=remaining_age*52 # remaining number of weeks
age_in_months=remaining_age*12 # remaining number of months
message=f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left ."
print(message)
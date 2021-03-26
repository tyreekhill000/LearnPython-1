#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")
bill_amount =float(input("What is the  bill amount\n"))
tip_as_percentage=int(input("What tip percentage would you like to give 10, 12, 15 ?\n"))
num_people_shared=int (input("With how many people the bill amount is shared\n"))
bill_amount_with_tip=bill_amount+(bill_amount*(tip_as_percentage/100))
sharing_amount=round(bill_amount_with_tip/num_people_shared,2)
print(f"Amount to be shared is {sharing_amount}")

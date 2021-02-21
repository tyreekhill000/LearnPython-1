number =100
for n in range(1,number+1):
    if(n%3==0 and n%5==0): #Divisible by both 3 and 5
        print("FizzBuz")
    elif n%3==0: # Divisible by 3
        print("Fiz")
    elif n%5==0: #Divisible by 5
        print("Buz")
    else:
        print(n)

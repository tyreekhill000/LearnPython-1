print("Leap Year Program")
year=int(input ("Enter the Year"))
if year%4:
     print(f"{year} is a leap year")
else:
     if year%100:
         if year%400:
            print(f"{year} is a leap year")
         else:
            print(f"{year} is not a leap year")
     else:
         print(f"{year} is not a leap year")



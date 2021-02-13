print("Leap Year Program")
year=int(input ("Enter the Year"))
year_four=year%4
year_100=year%100
year_400=year%400
print(f"year/4=={year_four} ,Year_100=={year_100}, Year_400={year_400}")
if year%4 ==0:
     if year%100==0:
         if year%400 ==0:
            print(f"{year} is a leap year")
         else:
            print(f"{year} is not a leap year")
     else:
          print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")



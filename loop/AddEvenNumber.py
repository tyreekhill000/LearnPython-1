number=100
##Using range and step
sum=0
for n in range(0,number+1,2):
    sum=sum+n;
print(sum)

#using range without step
sum1=0
for n in range(0,number):
    if(number%2==0):
      sum1=sum1+n;
print(sum)

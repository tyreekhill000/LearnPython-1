heights = input("Enter the heights that need to be added in the list").split()
for n in range(0,len(heights)):
    heights [n]= int (heights[n])

length=0
sum=0
for height in heights:
    length=length+1
    sum=sum+height

print(sum)
print(length)
avgheight=sum/length
print(f"average height is {avgheight}" )



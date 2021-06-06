import random
from random import randrange,randint,random,uniform

print (randint(1, 10)) # generate random integer number within the range both inclusive
print (randrange(1,10,2)) # generate random integer number within the range ie 1, 10 and then step over by 2

print (uniform(1,5))
print(random()) # generate random float between 0.0001... to 0.99999999 and it will not include 1
print(5*random()) # if you want to genrate a random float number with in 5

# print(random.randrange(1,10,2))
# print(randrange(1,10,2))
# for i in range(10):
#  print(randrange(0,10,2))



# sequence = [random.randint(0, i) for i in range(10)]
# print (sequence)


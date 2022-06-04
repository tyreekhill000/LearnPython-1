cars = ["Tesla", "Toyota", "Honda", "Subaru", "Hyundai"]
# This function returns the index of the first occurrence of value mentioned in arguments.
print(cars.index("Toyota"))
cars2 = cars[2:]

print(cars2)
#startingpt = input("where do you want your array to start from?: ")
#print(startingpt)
#start = cars.index(startingpt)
#cars3 = cars[start+1:]
def rotate(rotation):
    cars5 = cars[rotation+1:]+cars[0:rotation+1]
    print(cars5)
rotation = int(input("how many time do you want to rotate the list?: "))
rotate(rotation)


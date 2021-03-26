# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function with input and run your code.
def greet(name,location):
    print(f"Hello {name}")
    print(f"Do you live in  {location}")
    print("Do you play cricket")
greet("Pravin","Chennai")  #Positional arguments
greet(location="Chennai", name="Pravin")  #Keyword arguments

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2


operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
  }


first_number= int (input("Enter the first number\n"))
second_number= int (input("Enter the second number\n"))
for key in operations:
  print(f"{key}")
operation_symbol=input("What is the operation you would like to perform?\n")
calculation_function=operations[operation_symbol]
answer=calculation_function(first_number,second_number)
print(f"{first_number} {operation_symbol} {second_number} = {answer}")
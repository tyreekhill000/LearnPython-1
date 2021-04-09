def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

from art import logo
print (logo)
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
  }


num1= int (input("Enter the first number:\t"))
for key in operations:
 print(f"{key}")
to_continue=True
while to_continue :
    operation_symbol=input("What is the operation you would like to perform?\n")
    num2= int (input(f"Enter another number to  {operations[operation_symbol].__name__} with {num1}: \t"))
    calculation_function=operations[operation_symbol]
    answer=calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}\n")
    test=input (f"Type Y to continue operation with {answer}\n")
    if(test=='Y'):
      to_continue=True
      num1=answer
    else:
      to_continue=False


  

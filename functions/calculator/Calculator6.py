def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

from art import logo
from replit import clear
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
  }

def calculator():
  print (logo)
  num1= float (input("Enter the first number:\t"))
  for key in operations:
   print(f"{key}")
  to_continue=True
  while to_continue :
      operation_symbol=input("What is the operation you would like to perform?\n")
      num2= float (input(f"Enter another number to  {operations[operation_symbol].__name__} with {num1}: \t"))
      calculation_function=operations[operation_symbol]
      answer=calculation_function(num1,num2)
     
     
      print(f"{num1} {operation_symbol} {num2} = {answer}\n")
      test=input (f"Type Y to continue operation with {answer} and N to start to a new operation \n")
      if(test=='Y'):
        to_continue=True
        num1=answer
      elif (test=='N'):
        to_continue=False
        clear()
        calculator() # recursive function call
      else:
        clear()
        exit()
        
calculator()

  

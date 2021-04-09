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


first_number= int (input("Enter the first number\n"))
second_number= int (input("Enter the second number\n"))
for key in operations:
 print(f"{key}")

operation_symbol=input("What is the operation you would like to perform?\n")
calculation_function=operations[operation_symbol]
answer=calculation_function(first_number,second_number)
print(f"{first_number} {operation_symbol} {second_number} is  {answer}" )
mid_answer=answer
to_continue=True
while to_continue :
  test=input (f"Type Y to continue operation with {mid_answer}\n")
  if(test=='Y'):
    operation_symbol=input("pick up another operation\n")
    calculation_function=operations[operation_symbol]
    another_number= int (input(f"Enter the  another number to {operations[operation_symbol].__name__} with {mid_answer} \n"))
    print(f"{mid_answer} {operation_symbol} {another_number}")
    mid_answer=calculation_function(mid_answer,another_number)
    print(f" is {mid_answer}")
  else:
    to_continue=False


  

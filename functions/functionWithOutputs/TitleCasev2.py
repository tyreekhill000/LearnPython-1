#function with miltiple returns.
#function with docStrings

def format_name(first_name, last_name):
  """ Take a first_name and last_name and 
  format it to return the title case version of the name"""
  # Early exit
  if first_name =="" or last_name=="":
   return "Your first and last name is empty"

  formatted_first_ame=first_name.title()
  formatted_last_name=last_name.title()
 
  return f"formatted name is {formatted_first_ame} {formatted_last_name}"

f_name=input("What is the firstname?\n")
l_name=input("What is the lastname?\n")
#print (format_name(f_name,l_name))
formatted_name=format_name(f_name,l_name)
print(formatted_name)
#Other python built in function that retruns output
output=len(formatted_name)
print(output)

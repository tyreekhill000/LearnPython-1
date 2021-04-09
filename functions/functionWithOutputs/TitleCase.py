def format_name(first_name, last_name):
 formatted_first_ame=first_name.title()
 formatted_last_name=last_name.title()
 return f"formatted name is {formatted_first_ame} {formatted_last_name}" # returns the string to the caller format_name(f_name,l_name)

f_name=input("What is the firstname?\n")
l_name=input("What is the lastname?\n")
print (format_name(f_name,l_name))

#assign to variable 
formatted_name=format_name(f_name,l_name)
print(formatted_name)
# numeric_str = "½"
# print(numeric_str.isnumeric())  

# names = "Bob,Ann,Joe,Mike,Melissa,Erica"
# names_list = names.split(",")
# print(names_list)



# name = input("Enter first and last name:")
# while(name.find(" ") == -1 or len(name) < 3 ):
#     name = input("Incorrect. Enter first and last name:")

# # must start with digit
# street = input("Enter street: ")
# while(len(street) == 0 or not street[0].isdigit()):
#     street = input("Incorrect. Enter street: ")

# # must be two characters
# state = input("Enter state (two char): ")
# while(len(state) != 2 or not state.isalpha()):
#     state = input("Incorrect. Enter state: ")

# zip = input("Enter zip (5 digits): ")
# while(len(zip) != 5 or not zip.isdigit()):
#     zip = input("Incorrect. Enter zip: ")

# print(name.upper(), "\n", street.upper(), "\n", state.upper(), " " , zip)

import re
txt = "ay Today is the day ay"
match = re.findall(r"[kdr]ay", txt)
print(match)
print(len(match))
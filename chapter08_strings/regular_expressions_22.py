import testg

test.test()

# numeric_str = "½" 
# print(numeric_str.isnumeric())  

# sentence = "Python,is,my,favorite,language,ever."

# tokens = sentence.split(",")
# print(tokens)

# firstAndLast = input("Enter first and last name: ")
# while " " not in firstAndLast.strip() or len(firstAndLast.strip()) < 3:
#      firstAndLast = input("Incorrect. Enter first and last name: ")

# street = input("Enter street address: ")
# while not street[0].isdigit() or len(street.strip()) < 5:
#      street = input("Incorrect. Enter street address: ")

# city = input("Enter city name: ")
# while len(city.strip()) < 3:
#      city = input("Incorrect. Enter city name: ")
    
# state = input("Enter state (two char): ")
# while len(state.strip()) != 2 or not state.isalpha():
#      state = input("Incorrect. Enter state: ")

# zip = input("Enter zip (5 digits only): ")
# while len(zip.strip()) != 5 or not zip.isdigit():
#      zip = input("Enter zip (5 digits only): ")


# print(firstAndLast.upper())
# print(street.upper())
# print(city.upper(), ", ", state.upper(), " ", zip)

import re

txt = " ay Today is the day may ray ay"
match = re.findall(r"[dm]ay", txt)
print(match)
print(len(match)) # prints 2
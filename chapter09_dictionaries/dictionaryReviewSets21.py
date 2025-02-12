# Dictionary and Set practice

# my_dict = {'a': 1, 'b': 2}
# #print(my_dict['c'])
# #del my_dict['c']
# my_dict.popitem()
# my_dict.popitem()
# my_dict.popitem() # throws error
#print(my_dict.get('c', 3))
#print(my_dict)
#my_dict.setdefault('c', 3)
#print(my_dict)

lines =[]
# Create a dictionary from the file provided. Use abbreviations as keys, and cities as values.
with open("datafiles/states.txt") as infile:
    lines = infile.readlines()

#print(lines)

states = {}
for aline in lines:
    value, key = aline.strip().split(",")
    states[key] = value

#print(states)

states["PR"] = "San Juan"

# Remove a state
# if "PR" in states:
#     del states["PR"]

states.pop("PR")
print(states)
print(states.pop("PR", None))

# Iterate through the dictionary printing keys and values
for key, value in states.items():
    print(f"The capitol of {key} is {value}.")
# Do the same, but sort by keys. (hint: sorted)
for value in sorted(states.values()):
    print(f"The capitol of {value}.")

# Get list or dictionary of states if the first letter starts with A (use dictionary comprehension)
#result = {for astate in states if astate[0] == "A" }
result = [astate for astate in states if astate.startswith("A") ]
print(result)
result = {key:value for key, value in states.items() if key.startswith("A")}
print(result)

movie_me = {"The Matrix", "Up", "It", "Us", "Alien", "E.T."}
movie_you = {"Signs", "Sixth Sense", "It", "Glass", "Alien", "Split"}

# all movies
print(movie_me | movie_you)
print(movie_me & movie_you)
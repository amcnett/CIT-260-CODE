# Dictionary and Set practice

my_dict = {'a': 1, 'b': 2} 
#print(my_dict.get('c', 3))
# print(my_dict.get('c'))
# print(my_dict['c'])
#del my_dict['c'] # throws error if does not exist

print(my_dict.pop('c', None))
lines = []
# Create a dictionary from the file provided. Use abbreviations as keys, and cities as values.
with open("states.txt") as infile:
    lines = infile.readlines()
print(lines)

states = {}
for aline in lines:
    value, key = aline.strip().split(",")
    states[key] = value
print(states)

# Add a state
states["PA"] = "Williamsport"
print(states)
# Remove a state
states.pop("zz", None)
states.pop("zz", None)
states.pop("zz", None)
# Iterate through the dictionary printing keys and values
for key,value in states.items():
    print(f"The capitol of {key} is {value}")
# Do the same, but sort by keys. (hint: sorted)
for key in sorted(states):
    print(key)

for val in sorted(states.values()):
    print(val)

# Get list of states if the first letter starts with A (use dictionary comprehension)
#a_list = [key for key in states if key.startswith("A")]
a_list = [key for key in states if key[0] == "A"]
print(a_list)

a_list = {key:value for key,value in states.items() if key[0] == "A"}
print(a_list)
#resulting expression
#for loop
#filtering if

# Create two sets. One set should contain a list of movies you like, 
# the other should contain a list of movies your neighbor likes.​
# List all movies​
# Find movies that you both like ​
# Find movies that only you like​
# Find movies that only your neighbor likes

movie_me = {"The Matrix", "Up", "It", "Us", "Alien", "E.T."}
movie_you = {"Signs", "Sixth Sense", "It", "Glass", "Alien", "Split"}

# List all movies​
print(movie_me | movie_you)

# List movies that we both like​
print(movie_me  & movie_you)
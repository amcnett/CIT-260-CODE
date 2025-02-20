# Problem 1: Find the Largest Element
# Write a function that takes a 2D list and returns the largest element in the list.
def get_largest(x):
 return max(x)

alist = [23, 5, 454, 654, 34, 2]
print(get_largest(alist))

# Problem 2: Find the Largest Element (Again)
# Find the max value in the tuple below and display it:
atup = (23, 5, 454, 654, 34, 2)
max_val = max(atup)
print(max_val)

# t = (5, 1, 8, 4, 2)
# Problem 3: Temp Conversion (back again!)
# Write a list comprehension that takes a list of temperatures in Celsius and converts them to Fahrenheit and provides the resulting list.

# Formula: Fahrenheit = Celsius * (9/5) + 32

# Example: Input: [0, 20, 37, 100] Output: [32, 68, 98.6, 212]

tempsincel = [0, 20 , 37, 100]
fahr = [i * (9/5) + 32 for i in tempsincel]
print(fahr)

# Problem 4: Find the Longest Word
# Find the longest word in the string.

# Example: Input: "The quick brown fox jumps over the lazy dog" Output: "jumps"

my_input = "The quick brown fox jumps over the lazy dog"
words = my_input.split(" ")
longest = ""
for word in words:
 if len(word) >= len(longest):
  longest = word

print(longest) 

# Problem 5: Count Words in a String
# Count and print the number of words in a given string.
my_input = "The quick brown fox jumps over the lazy dog"
print(len(my_input.split()))


# Example: Input: "The quick brown fox jumps over the lazy dog" Output: 9
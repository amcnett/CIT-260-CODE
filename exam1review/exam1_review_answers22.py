# Problem 1: Find the Largest Element
# Write a function that takes a 2D list and returns the largest element in the list.
alist = [23, 35, 243, 556, 67, 234]
maxvalue = max(alist)
print(maxvalue)
# Problem 2: Find the Largest Element (Again)
# Find the max value in the tuple below and display it:
t = (5, 1, 8, 4, 2)
print(max(t))
# Problem 3: Temp Conversion (back again!)
# Write a list comprehension that takes a list of temperatures in Celsius and converts them to Fahrenheit and provides the resulting list.
# Formula: Fahrenheit = Celsius * (9/5) + 32
# Example: Input: [0, 20, 37, 100] Output: [32, 68, 98.6, 212]
cel = [0, 20, 37, 100]
fahr = [temp * 9/5 + 32 for temp in cel]
print(fahr)
fahr = [temp * 9//5 + 32 for temp in cel]
print(fahr)
# Problem 4: Find the Longest Word
# Find the longest word in the string.
# Example: Input: "The quick brown fox jumps over the lazy dog" Output: "jumps"
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)

# 
print(max(sentence.split(), key=len))

# Problem 5: Count Words in a String
# Count and print the number of words in a given string.
# Example: Input: "The quick brown fox jumps over the lazy dog" Output: 9
sentence = "The quick brown fox jumps over the lazy dog"
print(len(sentence.split(" ")))
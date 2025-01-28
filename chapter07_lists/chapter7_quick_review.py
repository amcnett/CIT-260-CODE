# Section 21 Review
matrix = [[1,2,3], [5,6,7], [4,8,9]]

print(matrix[2][0])

# change an element
matrix[2][0] = 7

# last element in the 2d list
print(matrix[2][2])

print(matrix)

# sum of second nested list
print(sum(matrix[1]))

atuple = (1,2,3,4)
#atuple[0] = 0  # cannot do this 

sentence = "Question or comments can be sent to someone@pct.edu today. Please allow 24 hours for a response."
words = sentence.lower().split()
print(words)
for word in words:
    if "@" in word:
        print(word)

# Section 22 review
matrix = [[12, 23, 45, 56], [87, 99, 32, 19, 300]]

# access first element and update the value
matrix[0][0] = 0

# print the last element
print(matrix[1][4])

# sum the first nested list
print(sum(matrix[0]))
print(matrix)

atuple = (1,2,[0,1])
# atuple[0] = 0  # cannot do this
atuple[2].append(2) # but can do this
print(atuple)

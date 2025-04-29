# guess the category
# can you fix the errors?

import random

# Dictionary with categories and words
categories = {
    "Fruits": ["Apple", "Banana", "Cherry", "Grape", "Orange"]
    "Animals": ["Lion", "Elephant", "Kangaroo", "Panda", "Dolphin"]
    "Minecraft": ["Biome", "Mobs", "Enderman", "Redstone", "Nether"]
    "Memes": ["Success Kid", "Grumpy Cat", "Distracted Boyfriend", "Philosoraptor"]
}

# Select a random word from one of the categories
category, words = random.choice(list(categories.items()))
word = random.choice(words)

print("Welcome to the Word Category Quiz!")
print(f"Which category does this word belong to? -> {word}")

# Display categories for selection
options = list(categories.values())
i = 0
for option in options:
    print(f"{i}. {option}")
    i+=1

# Get user input
choice = input("Enter the number of the correct category: ").strip()

# Check answer
if choice.isdigit() and 1 <= int(choice) <= len(options):
    selected_category = options[int(choice) - 1]
    if selected_category == category:
        print("Correct! 🎉")
    else:
        print(f"Wrong! The correct category was '{category}'.")
else:
    print("Invalid input! Please enter a number from the options.")

print("Thanks for playing!")
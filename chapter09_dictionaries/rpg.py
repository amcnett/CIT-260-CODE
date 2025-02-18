# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# dict1 |= dict2
# print(dict1)

newlist = [char.upper() for char in "hello" if char != 'e']
print(newlist)

import pickle, random

scores_player = {
    "win": 0,
    "tie": 0,
    "lost": 0
}

# load any existing player stats
try:
    with open("scores.dat", "rb") as infile:
        scores_player = pickle.load(infile)
        print("Welcome back!")
except FileNotFoundError:
    print("Welcome New Player!")

print(scores_player)

options = ["Rock", "Paper", "Scissors"]
playAgain = "Y"

# core game loop
while playAgain == "Y":

    #computer choice
    choice = random.randint(0, 2)
    computer_choice = options[choice]

    #alternative to setting computer choice
    #computer_choice = random.choice(options)

    player_choice = input("Enter Rock, Paper, or Scissors: ")

    while player_choice not in options: # validation
        player_choice = input("Invalid Option. Enter Rock, Paper, or Scissors: ")

    if player_choice == computer_choice:
        print("It's a tie!")
        scores_player["tie"] += 1
    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
        scores_player["win"] += 1
    elif player_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
        scores_player["win"] += 1
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
        scores_player["win"] += 1
    else:
        print("Computer wins!")
        scores_player["lost"] += 1

    playAgain = input("Enter Y to play again: ").upper()

print(scores_player)
with open("scores.dat", "wb") as outfile:
    pickle.dump(scores_player, outfile)
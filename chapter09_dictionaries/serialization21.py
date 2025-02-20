import pickle, random

player_score = {
    "win": 0, 
    "ties": 0, 
    "lost": 0
}

computer_score = {
    "win": 0, 
    "ties": 0, 
    "lost": 0
}

def updateScores():
    # update scores here
    return

# load the previous scores
with open("scores.dat", "rb") as infile:
    player_score = pickle.load(infile)
    computer_score = pickle.load(infile)

print(player_score)
print(computer_score)

playAgain = "y"
options = ["Rock", "Paper", "Scissors"]

while playAgain == "y":
    # determine computer choice
    #num = random.randint(0, 2)
    #computer_choice = options[num]
    computer_choice = random.choice(options)

    # determine player choice
    player_choice = input("Enter Rock, Paper, or Scissors: ").strip().capitalize()
    while player_choice not in options:
        player_choice = input("Invalid option. Enter Rock, Paper, or Scissors: ").strip().capitalize()

    print(f"You entered {player_choice} and computer picked {computer_choice}.")
    # print winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif player_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    else:
        print("Computer wins!")

    playAgain = input("Play again (Y or N): ").strip().lower()
    while playAgain != "y" and playAgain != "n":
        playAgain = input("Invalid input. Play again (Y or N): ").strip().lower()

with open("scores.dat", "wb") as outfile:
    pickle.dump(player_score, outfile)
    pickle.dump(computer_score, outfile)
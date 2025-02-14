import pickle

# player_stat = {
#     "win": 0,
#     "tie": 0,
#     "lost": 0
# }

# computer_stat = {
#     "win": 0,
#     "tie": 0,
#     "lost": 0
# }

# with open("scores.dat", "wb") as outfile:
#     pickle.dump(player_stat, outfile)
#     pickle.dump(computer_stat, outfile)

# read existing scores
with open("scores.dat", "rb") as infile:
    scores_player = pickle.load(infile)
    scores_computer = pickle.load(infile)

print(scores_player)
print(scores_computer)
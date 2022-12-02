from rich import print

with open("input", "r") as f:
    data = f.read().splitlines()

win = ["C Z", "A Z", "B Z"]
lose = ["B X", "C X", "A X"]
draw = ["A Y", "B Y", "C Y"]

# Col 1
# A = Rock
# B = Paper
# C = Scissors

# Col 2
# X = Rock      +1
# Y = Paper     +2
# Z = Scissors  +3

# X = Lose
# Y = Draw
# Z = Win

wins = []
losses = []
draws = []

for line in data:
    if line in win:
        wins.append(line)
    if line in lose:
        losses.append(line)
    if line in draw:
        draws.append(line)

print(len(wins))
print(len(losses))
print(len(draws))


win_count = {i: wins.count(i) for i in wins}
loss_count = {i: losses.count(i) for i in losses}
draw_count = {i: draws.count(i) for i in draws}

print(win_count)

for k, v in win_count.items():
    if "A" in k:
        ascore = v * 6 + v * 2
    if "B" in k:
        bscore = v * 6 + v * 3
    if "C" in k:
        cscore = v * 6 + v * 1
win_score = ascore + bscore + cscore

for k, v in draw_count.items():
    if "A" in k:
        ascore = v * 3 + v * 1
    if "B" in k:
        bscore = v * 3 + v * 2
    if "C" in k:
        cscore = v * 3 + v * 3
draw_score = ascore + bscore + cscore

for k, v in loss_count.items():
    if "A" in k:
        ascore = v * 3
    if "B" in k:
        bscore = v * 1
    if "C" in k:
        cscore = v * 2
loss_score = ascore + bscore + cscore

total_score = win_score + loss_score + draw_score

print(total_score)

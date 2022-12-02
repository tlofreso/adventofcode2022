from rich import print

with open("input", "r") as f:
    data = f.read().splitlines()

win = ['C X', 'A Y', 'B Z']
lose = ['B X', 'C Y', 'A Z']
draw = ['A X', 'B Y', 'C Z']

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

win_count = {i:wins.count(i) for i in wins}
loss_count = {i:losses.count(i) for i in losses}
draw_count = {i:draws.count(i) for i in draws}

for k, v in win_count.items():
    if 'X' in k:
        xscore = v * 6 + v * 1
    if 'Y' in k:
        yscore = v * 6 + v * 2
    if 'Z' in k:
        zscore = v * 6 + v * 3
win_score = xscore + yscore + zscore

for k, v in draw_count.items():
    if 'X' in k:
        xscore = v * 3 + v * 1
    if 'Y' in k:
        yscore = v * 3 + v * 2
    if 'Z' in k:
        zscore = v * 3 + v * 3
draw_score = xscore + yscore + zscore

for k, v in loss_count.items():
    if 'X' in k:
        xscore = v * 1
    if 'Y' in k:
        yscore = v * 2
    if 'Z' in k:
        zscore = v * 3
loss_score = xscore + yscore + zscore

total_score = win_score + loss_score + draw_score

print(total_score)
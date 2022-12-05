import re
from rich import print

with open("input", "r") as f:
    crates, moves = f.read().split("\n\n")

num_crates = crates.split("\n")[-1]

crates = {
    1: ["N", "T", "B", "S", "Q", "H", "G", "R"],
    2: ["J", "Z", "P", "D", "F", "S", "H"],
    3: ["V", "H", "Z"],
    4: ["H", "G", "F", "J", "Z", "M"],
    5: ["R", "S", "M", "L", "D", "C", "Z", "T"],
    6: ["J", "Z", "H", "V", "W", "T", "M"],
    7: ["Z", "L", "P", "F", "T"],
    8: ["S", "W", "V", "Q"],
    9: ["C", "N", "D", "T", "M", "L", "H", "W"],
}

all_moves = []
for move in moves.split("\n"):
    move = re.findall(r"\d+", move)
    all_moves.append([int(i) for i in move])


def move_crates(qty, start, end):
    while qty > 0:
        crates[end].insert(0, crates[start].pop(0))
        qty -= 1


for move in all_moves:
    qty = move[0]
    start = move[1]
    end = move[2]
    move_crates(qty, start, end)


order = []
for crate in crates.values():
    order += crate[0]

print("".join(order))

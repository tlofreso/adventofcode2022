from rich import print

with open("input", "r") as f:
    data = f.read().split("\n\n")

cal_sums = []
for elf in data:
    elf = elf.split()
    cal_sums.append(sum([int(x) for x in elf]))

cal_sums.sort()

# Answer:
print("Puzzle 1: " + str(cal_sums[-1]))
print("Puzzle 2: " + str(sum(cal_sums[-3:])))

from rich import print

with open("input", "r") as f:
    data = f.read().splitlines()


def overlaps(list):
    shortest = min(list, key=len)
    longest = max(list, key=len)

    if shortest == longest:
        return any(item in list[0] for item in list[1])

    result = any(item in longest for item in shortest)

    return result


pair_ranges = []
for line in data:
    pairs = line.split(",")
    pair1 = [int(i) for i in pairs[0].split("-")]
    pair2 = [int(i) for i in pairs[1].split("-")]
    range1 = []
    range2 = []

    for n in range(pair1[0], pair1[1] + 1):
        range1.append(n)
    for n in range(pair2[0], pair2[1] + 1):
        range2.append(n)

    pair_ranges.append([range1, range2])

t = 0
for range in pair_ranges:
    if overlaps(range) is True:
        t += 1

print(t)

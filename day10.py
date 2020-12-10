from collections import Counter

with open("day10.txt") as input:
    adapters = []
    for a in input.readlines():
        adapters.append(int(a))
adapters.sort()
target_joltage = adapters[-1] + 3
adapters.append(target_joltage)

diffs = []
current_joltage = 0
for a in adapters:
    diffs.append(a - current_joltage)
    current_joltage = a

count = Counter(diffs)

print(f"Part 1: {count[1]} * {count[3]} = {count[1] * count[3]}")

arrangements = {0: 1}

for a in adapters:
    z = arrangements.get(a - 1, 0)
    y = arrangements.get(a - 2, 0)
    x = arrangements.get(a - 3, 0)
    arrangements[a] = x + y + z

print(f"Part 2: {arrangements[target_joltage]}")

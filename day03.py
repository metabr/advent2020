INPUT = "day03.txt"

with open(INPUT) as input:
    pattern = input.readlines()
    size_x = len(pattern[0].strip("\n"))
    size_y = len(pattern)


def next_pos(pos, step_x, step_y):
    x, y = pos
    x += step_x
    if x >= size_x:
        x = x - size_x
    y += step_y
    return (x, y)


def count_trees_for_slope(step_x, step_y):
    print(f"Right {step_x}, down {step_y}:")

    pos = (0, 0)
    num_trees = 0

    while pos[1] < size_y:
        x, y = pos
        # print(f"at position {pos}: {pattern[y][x]}")
        if pattern[y][x] == "#":
            num_trees += 1
        pos = next_pos(pos, step_x, step_y)

    print(f"encountered {num_trees} trees")
    return num_trees


a = count_trees_for_slope(1, 1)
b = count_trees_for_slope(3, 1)
c = count_trees_for_slope(5, 1)
d = count_trees_for_slope(7, 1)
e = count_trees_for_slope(1, 2)

print(f"Multiplied together: {a * b * c * d * e}")

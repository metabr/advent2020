import re


def parse_bag(line):
    color, contains = re.split(" bags contain ", line)
    r = {}
    for c in re.split(" bags?,? ", contains):
        result = re.findall("(\d) (\w+ \w+)", c)
        if len(result) > 0:
            count, col = result[0]
            r[col] = int(count)
    return (color, r)


bags = {}
with open("day07.txt") as input:
    for line in input.readlines():
        col, cont = parse_bag(line)
        bags[col] = cont


def direct_contains(colors):
    result = set()
    for bag_color, contains in bags.items():
        for color in colors:
            if color in contains.keys():
                result.add(bag_color)
    return result

# Part 1
result = direct_contains(["shiny gold"])
n_colors = 0
while len(result) > n_colors:
    n_colors = len(result)
    result = result.union(direct_contains(result))

print(f"Bags that can contain shiny gold bags: {len(result)}")

# Part 2
def count_bags_inside(col):
    result = 0
    for next_col, count in bags[col].items():
        result += count
        result += count * count_bags_inside(next_col)
    return result

print(f"Bags inside shiny gold one: {count_bags_inside('shiny gold')}")

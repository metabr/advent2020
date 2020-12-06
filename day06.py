def unique_answers(group):
    all_answers = "".join(group)
    unique_answers = set(all_answers)
    return len(unique_answers)


def common_answers(group):
    common = set(group[0])
    for answer in group:
        common = common.intersection(answer)
    return len(common)


with open("day06.txt") as input:
    declarations = [[]]
    new_group = True

    for line in input.readlines():
        line = line.strip("\n")
        if line == "":
            new_group = True
            declarations.append([])
        elif new_group == True:
            declarations[-1].append(line)
            new_group = False
        else:
            declarations[-1].append(line)

sum_unique = 0
sum_common = 0

for group in declarations:
    sum_unique += unique_answers(group)
    sum_common += common_answers(group)

print(f"Sum of the answers counted for part 1: {sum_unique}")
print(f"Sum of the answers counted for part 2: {sum_common}")

import re


INPUT = "day02.txt"


def parse_entry(entry):
    min_max, letter, pwd = entry.strip("\n").split(" ")
    _min, _max = min_max.split("-")
    _min = int(_min)
    _max = int(_max)
    return {
        "min": _min,
        "max": _max,
        "letter": letter.strip(":"),
        "password": pwd,
    }


def is_valid(entry):
    parsed = parse_entry(entry)
    count = len(re.findall(parsed["letter"], parsed["password"]))
    if count >= parsed["min"] and count <= parsed["max"]:
        return True
    return False


def is_valid2(entry):
    parsed = parse_entry(entry)
    c = parsed["letter"]
    pos1_idx = parsed["min"] - 1
    pos2_idx = parsed["max"] - 1
    c1 = parsed["password"][pos1_idx]
    c2 = parsed["password"][pos2_idx]
    if (c == c1 and c != c2) or (c != c1 and c == c2):
        return True
    return False


with open(INPUT) as input:
    lines = input.readlines()

result = 0
result2 = 0

for line in lines:
    if is_valid(line):
        result += 1
    if is_valid2(line):
        result2 += 1

print(result)
print(result2)

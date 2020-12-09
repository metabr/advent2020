INPUT = "day01.txt"

ns = []


def find_numbers(ns, desired_sum=2020):
    for n in ns:
        target = desired_sum - n
        if target in ns:
            return (n, target)
    return False


with open(INPUT) as input:
    ns = [int(x) for x in input.read().split("\n")]

n1, n2 = find_numbers(ns)

print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} * {n2} = {n1 * n2}")

# find three numbers

for n in ns:
    subtarget = 2020 - n
    result = find_numbers(ns, subtarget)
    if result:
        n2, n3 = result
        print(f"{n} + {n2} + {n3} = {n + n2 + n3}")
        print(f"{n} * {n2} * {n3} = {n * n2 * n3}")
        exit(0)

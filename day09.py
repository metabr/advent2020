ns = []
with open("day09.txt") as input:
    for line in input.readlines():
        ns.append(int(line))

preamble_length = 25
preamble = ns[:preamble_length]
rest = ns[preamble_length:]

print(ns)
print(preamble)
print(rest)


def is_sum_of_pair(n, ns):
    print(f"is {n} a sum of two of {ns}?")
    for n_ in ns:
        if n_ < n:
            nt = n - n_
            if nt in ns and nt != n_:
                print(f"Yes, {nt} + {n_} == {n}!")
                return True
    print("Nope.")
    return False


def find_sequence(n, ns):
    t = ns[:1]
    for i in range(2, len(ns)):
        if sum(t) == n:
            return t
        elif sum(t) > n:
            return False
        t = ns[:i]
    return False


for i in range(len(rest)):
    n = rest[0]
    if is_sum_of_pair(n, preamble):
        preamble.append(n)
        del preamble[0]
        del rest[0]
    else:
        print(f"Number {n} is not sum of previous {preamble_length} numbers.")
        break

for i in range(len(ns) - 1):
    r = find_sequence(n, ns[i:])
    if r and n not in r:
        print(f"Resulting sequence: {r}")
        min_ = min(r)
        max_ = max(r)
        print(f"{min_} + {max_} = {min_ + max_}")

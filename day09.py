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

for i in range(len(rest)):
    n = rest[0]
    if is_sum_of_pair(n, preamble):
        preamble.append(n)
        del preamble[0]
        del rest[0]
    else:
        print(f"Number {n} is not sum of previous {preamble_length} numbers.")
        break

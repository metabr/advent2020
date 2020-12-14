import re


def parse_mem(s):
    addr = int(s.split("[")[-1].split("]")[0])
    val = int(s.split("=")[-1])
    return (addr, val)


def parse_mask(s):
    mask = re.findall(".*= ([10X]+)", s).pop()
    return mask


def input(filename="day14.txt"):
    with open(filename) as input:
        return input.readlines()


def apply_mask(val, mask):
    val = list("{0:036b}".format(val))
    for i in range(len(val)):
        if mask[i] != "X":
            val[i] = mask[i]
    return int("".join(val), 2)


if __name__ == "__main__":
    program = input()
    mask = "".join(["X" for _ in range(36)])
    mem = {}

    for instr in program:
        if instr.startswith("mask"):
            mask = parse_mask(instr)
        else:
            addr, val = parse_mem(instr)
            mem[addr] = apply_mask(val, mask)

    print(f"Sum of values in memory: {sum(mem.values())}")

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


def int_to_list(n):
    s = "{0:036b}".format(n)
    return list(s)


def list_to_int(n):
    return int("".join(n), 2)


def apply_mask(val, mask):
    val = int_to_list(val)
    for i in range(len(val)):
        if mask[i] != "X":
            val[i] = mask[i]
    return list_to_int(val)


def flip(addr, offset):
    addr = int_to_list(addr)
    if addr[offset] == "0":
        addr[offset] = "1"
    else:
        addr[offset] = "0"
    return list_to_int(addr)


def decode(addr, mask):
    addr = int_to_list(addr)
    for i in range(len(addr)):
        if mask[i] == "1":
            addr[i] = "1"
    result = [addr]
    for i in range(len(addr)):
        if mask[i] == "X":
            for j in range(len(result)):
                x = result[j]
                x = list_to_int(x)
                r = flip(x, i)
                r = int_to_list(r)
                result.append(r)
    return [list_to_int(x) for x in result]


if __name__ == "__main__":
    program = input()
    mask = "".join(["X" for _ in range(36)])
    mem = {}

    for instr in program:
        if instr.startswith("mask"):
            mask = parse_mask(instr)
        else:
            addr, val = parse_mem(instr)
            decoded_addrs = decode(addr, mask)
            for a in decoded_addrs:
                mem[a] = val

    print(f"Sum of values in memory: {sum(mem.values())}")

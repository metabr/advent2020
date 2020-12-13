from math import prod

def input(timetable):
    items = timetable.split(",")
    return {i: int(bus) for i, bus in enumerate(items) if bus != "x"}


if __name__ == "__main__":
    i = input("37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,457,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,431,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19")
    N = prod(i.values())
    t = sum((m - r) * N // m * pow(N // m, -1, m) for r, m in i.items()) % N
    print(t)

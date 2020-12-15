def input(input="1,12,0,20,8,16"):
    d = {}
    l = []
    for i, a in enumerate(input.split(",")):
        a = int(a)
        l.append(a)
        if a in d.keys():
            d[a].append(i + 1)
        else:
            d[a] = [i + 1]
    return d, l


def number_to_add(d, l):
    last = l[-1]
    if len(d[last]) > 1:
        cur_pos = len(l)
        prev_pos = d[last][-2]
        new_number = cur_pos - prev_pos
        return new_number
    else:
        return 0


if __name__ == "__main__":
    d, l = input()

    while len(l) < 30000000:
    # while len(l) < 2020:
        n = number_to_add(d, l)
        l.append(n)
        if n in d.keys():
            d[n].append(len(l))
        else:
            d[n] = [len(l)]
    print(l[-1])

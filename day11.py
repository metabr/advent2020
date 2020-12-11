from collections import Counter


def read_seats():
    r = []
    with open("day11.txt") as input:
        for line in input.readlines():
            r.append(list(line.strip("\n")))
    return r


seats = read_seats()
size_y = len(seats[0])
size_x = len(seats)


def valid_position(pos):
    x, y = pos
    return x >= 0 and y >= 0 and x < size_x and y < size_y


def adjacent_positions(x, y):
    pos = []
    pos.append((x - 1, y + 1))
    pos.append((x, y + 1))
    pos.append((x + 1, y + 1))
    pos.append((x - 1, y))
    pos.append((x + 1, y))
    pos.append((x - 1, y - 1))
    pos.append((x, y - 1))
    pos.append((x + 1, y - 1))
    result = list(filter(valid_position, pos))
    return result


def adjacent_seats(pattern, x, y):
    seats = []
    for pos in adjacent_positions(x, y):
        x_, y_ = pos
        seats.append(pattern[x_][y_])
    return seats


def seats_in_direction(pattern, x, y):
    seats = []
    directions = [
        lambda x, y: (x, y + 1),
        lambda x, y: (x, y - 1),
        lambda x, y: (x + 1, y + 1),
        lambda x, y: (x + 1, y - 1),
        lambda x, y: (x - 1, y + 1),
        lambda x, y: (x - 1, y - 1),
        lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
    ]
    for d in directions:
        p = d(x, y)
        while valid_position(p):
            x_, y_ = p
            s = pattern[x_][y_]
            if s != ".":
                seats.append(s)
                break
            p = d(x_, y_)
    return seats


def print_seats(seats, filename=None):
    output = "\n".join(["".join(row) for row in seats])
    if filename:
        with open(filename, "w") as output_file:
            output_file.write(output)
            output_file.write("\n")
    else:
        print(output)


def occupied(seats):
    result = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                result += 1
    return result


def step(seats):
    r = [["." for i in range(size_y)] for j in range(size_x)]
    for x in range(size_x):
        for y in range(size_y):
            seat = seats[x][y]
            adj = seats_in_direction(seats, x, y)
            count = Counter(adj)
            if seat == "L" and not "#" in adj:
                r[x][y] = "#"
            elif seat == "#" and count["#"] >= 5:
                r[x][y] = "L"
            else:
                r[x][y] = seat
    return r


def out_file(i):
    return "output" + "%03d" % (i) + ".txt"


prev_occupied = -1
curr_occupied = occupied(seats)

print_seats(seats, out_file(0))
i = 1
while prev_occupied != curr_occupied:
    seats = step(seats)
    prev_occupied = curr_occupied
    curr_occupied = occupied(seats)
    #print_seats(seats, out_file(i))
    print_seats(seats)
    i += 1
    print(f"Occupied seats: {curr_occupied}")

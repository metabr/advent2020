def parse_row(boarding_pass):
    row = boarding_pass[:7]
    row = row.replace("B", "1").replace("F", "0")
    return int(row, 2)


def parse_column(boarding_pass):
    col = boarding_pass[-4:]
    col = col.replace("R", "1").replace("L", "0")
    return int(col, 2)


def seat_id(boarding_pass):
    return parse_row(boarding_pass) * 8 + parse_column(boarding_pass)


highest_seat_id = 0
seat_ids = []

with open("day05.txt") as input:
    for boarding_pass in input.readlines():
        id_ = seat_id(boarding_pass)
        seat_ids.append(id_)
        if id_ > highest_seat_id:
            highest_seat_id = id_

print(f"Highest seat id: {highest_seat_id}")

seat_ids.sort()
for i in range(len(seat_ids) - 1):
    if seat_ids[i + 1] != seat_ids[i] + 1:
        print(f"Seat between {seat_ids[i]} and {seat_ids[i+1]} is your seat, probably.")

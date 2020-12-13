def input(filename="day13.txt"):
    with open(filename) as input:
        earliest, timetable = input.readlines()
        buses = []
        for bus in timetable.split(","):
            if bus == "x":
                next
            else:
                buses.append(int(bus))
        return int(earliest), buses


def earliest_after(earliest, bus):
    t = 0
    while t < earliest:
        t += bus
    return t


if __name__ == "__main__":
    earliest, buses = input()
    timetable = {}
    for bus in buses:
        t = earliest_after(earliest, bus)
        print(f"next {bus}: {t}")
        timetable[bus] = t
    timetable = sorted(timetable.items(), key=lambda x: x[1])
    my_bus, my_time = timetable[0]
    print(
        f"bus id {my_bus} * ({my_time} - {earliest}) = {my_bus * (my_time - earliest)}"
    )

from collections import Counter


def neighbor_cubes(x, y, z):
    result = []
    for x_ in [x - 1, x, x + 1]:
        for y_ in [y - 1, y, y + 1]:
            for z_ in [z - 1, z, z + 1]:
                result.append((x_, y_, z_))
    result.remove((x, y, z))
    return result


class PocketDimension:
    def __init__(self):
        self.cubes = {}

    def activate(self, x, y, z):
        self.cubes[(x, y, z)] = "#"

    def deactivate(self, x, y, z):
        self.cubes[(x, y, z)] = "."

    def is_active(self, x, y, z):
        if self.cubes.get((x, y, z)) == "#":
            return True
        return False

    def get_neighbor_cubes(self, x, y, z):
        cubes = []
        for cx, cy, cz in neighbor_cubes(x, y, z):
            cubes.append(self.cubes.get((cx, cy, cz), "."))
        return cubes

    def active_neighbors(self, x, y, z):
        cubes = self.get_neighbor_cubes(x, y, z)
        count = Counter(cubes)
        return count["#"]

    def total_active(self):
        count = Counter(self.cubes.values())
        return count["#"]

    def range(self):
        xs = [0]
        ys = [0]
        zs = [0]
        for x, y, z in self.cubes.keys():
            xs.append(x)
            ys.append(y)
            zs.append(z)

        return (
            (min(xs) - 1, max(xs) + 1),
            (min(ys) - 1, max(ys) + 1),
            (min(zs) - 1, max(zs) + 1),
        )


def read_input(filename="day17.txt"):
    pd = PocketDimension()
    with open(filename) as input_file:
        lines = input_file.readlines()
        for y in range(len(lines)):
            for x in range(len(lines[0].strip("\n"))):
                if lines[y][x] == "#":
                    pd.activate(x, y, 1)
    return pd


if __name__ == "__main__":
    pd = read_input()

    for i in range(6):
        pd_next = PocketDimension()
        r = pd.range()
        x_min, x_max = r[0]
        y_min, y_max = r[1]
        z_min, z_max = r[2]
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    if pd.is_active(x, y, z):
                        n = pd.active_neighbors(x, y, z)
                        if n == 2 or n == 3:
                            pd_next.activate(x, y, z)
                    else:
                        n = pd.active_neighbors(x, y, z)
                        if n == 3:
                            pd_next.activate(x, y, z)
        pd = pd_next

    print(pd.total_active())

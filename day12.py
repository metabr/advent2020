def read_instructions(filename="day12.txt"):
    with open(filename) as input:
        return input.readlines()


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.wx = 1
        self.wy = 10

    def __str__(self):
        return f"I'm at ({self.x}, {self.y}) with waypoint {self.wx} norther and {self.wy} eastier"

    def N(self, arg):
        self.wx += arg

    def S(self, arg):
        self.wx -= arg

    def E(self, arg):
        self.wy += arg

    def W(self, arg):
        self.wy -= arg

    def l(self):
        x = self.wy
        y = -self.wx
        self.wx = x
        self.wy = y

    def r(self):
        x = -self.wy
        y = self.wx
        self.wx = x
        self.wy = y

    def R(self, arg):
        for _ in range(arg // 90):
            self.r()

    def L(self, arg):
        for _ in range(arg // 90):
            self.l()

    def F(self, arg):
        self.x += arg * self.wx
        self.y += arg * self.wy

    def handle_instruction(self, instruction):
        print(f"Instruction: {instruction}")
        op = instruction[0]
        arg = int(instruction[1:])

        getattr(self, op)(arg)

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


if __name__ == "__main__":
    instructions = read_instructions()
    ship = Ship()
    for instruction in instructions:
        ship.handle_instruction(instruction.strip("\n"))
        print(ship)
    print(f"Distance: {ship.manhattan_distance()}")

def read_instructions(filename="day12.txt"):
    with open(filename) as input:
        return input.readlines()


DIRECTIONS = ["N", "E", "S", "W"]

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = "E"

    def __str__(self):
        return f"I'm at ({self.x}, {self.y}) facing {self.facing}"

    def N(self, arg):
        self.x += arg

    def S(self, arg):
        self.x -= arg

    def E(self, arg):
        self.y += arg

    def W(self, arg):
        self.y -= arg

    def R(self, arg):
        current_pos = DIRECTIONS.index(self.facing)
        shift_pos = int(arg / 90)
        new_pos = (current_pos + shift_pos) % len(DIRECTIONS)
        self.facing = DIRECTIONS[new_pos]

    def L(self, arg):
        self.R(-arg)

    def F(self, arg):
        getattr(self, self.facing)(arg)

    def B(self, arg):
        self.R(180)
        self.F(arg)
        self.R(180)

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

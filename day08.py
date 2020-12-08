def parse(line):
    instruction, argument = line.strip("\n").split(" ")
    return (instruction, int(argument))

instructions = []
with open("day08.txt") as input:
    for line in input.readlines():
        instructions.append(parse(line))


class VM:
    def __init__(self, instructions):
        self.ip = 0
        self.acc = 0
        self.seen = []
        self.instructions = instructions
        self.terminated = False

    def add(self, arg):
        self.acc += arg
        self.ip += 1

    def jmp(self, arg):
        self.ip += arg

    def next(self):
        if self.ip == len(self.instructions):
            print("Successfully terminated.")
            self.terminated = True
            return

        print(f"ip: {self.ip}, acc: {self.acc}, next instruction: {self.instructions[self.ip]}")

        self.seen.append(self.ip)
        op, arg = self.instructions[self.ip]
        if op == "acc":
            self.add(arg)
        elif op == "jmp":
            self.jmp(arg)
        else:
            # nop
            self.ip += 1


def replace_first_instruction(instructions, start):
    instructions = instructions.copy()
    for i in range(start, len(instructions)):
        op, arg = instructions[i]
        if op == "nop" and arg != 0:
            new_instruction = ("jmp", arg)
            print(f"Replacing {instructions[i]} with {new_instruction} at offset {i}")
            instructions[i] = new_instruction
            return (instructions, i+1)
        elif op == "jmp":
            new_instruction = ("nop", arg)
            print(f"Replacing {instructions[i]} with {new_instruction} at offset {i}")
            instructions[i] = new_instruction
            return (instructions, i+1)
        i += 1
    return (instructions, i)

vm = VM(instructions)
start = 0

while not vm.terminated:
    if vm.ip in vm.seen:
        print(f"acc value: {vm.acc}")
        print("Loop detected, try to change instructions")
        new_instructions, start = replace_first_instruction(instructions, start)
        vm = VM(new_instructions)
    vm.next()

print(f"acc value: {vm.acc}")

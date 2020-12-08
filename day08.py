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

    def add(self, argument):
        self.acc += argument
        self.ip += 1

    def jmp(self, argument):
        self.ip += argument

    def next(self):
        print(f"ip: {self.ip}, acc: {self.acc}")
        if self.ip == len(self.instructions):
            print("Successful termination!")
            self.terminated = True
            return
        self.seen.append(self.ip)
        instruction, argument = self.instructions[self.ip]
        print(f"ins: {instruction}, arg: {argument}")
        if instruction == "acc":
            self.add(argument)
        elif instruction == "jmp":
            self.jmp(argument)
        else:
            self.ip += 1


def replace_first_instruction(instructions, start):
    instructions = instructions.copy()
    for i in range(start, len(instructions)):
        op, arg = instructions[i]
        if op == "nop" and arg != 0:
            instructions[i] = ("jmp", arg)
            return (instructions, i+1)
        elif op == "jmp":
            instructions[i] = ("nop", arg)
            return (instructions, i+1)
        i += 1
    return (instructions, i)

vm = VM(instructions)
start = 0

while not vm.terminated:
    if vm.ip in vm.seen:
        print("Loop detected, try to change instructions")
        new_instructions, start = replace_first_instruction(instructions, start)
        vm = VM(new_instructions)
    vm.next()

print(vm.acc)

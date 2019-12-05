import sys

input_file = 'input'
opcodes = [1, 2, 3, 4]

# Simple integer input
# No prompt and no error message for bad input
def get_int():
    x = input()
    while True:
        try:
            d = int(x)
        except ValueError:
            x = input()
            continue
        break
    return d

def add_or_mult(memory, oper, left, right, result):
    if oper // 100 % 10 == 0:
        left = memory[left]
    if oper // 1000 % 10 == 0:
        right = memory[right]
    if oper % 100 == 1:
        memory[result] = left + right
    else:
        memory[result] = left * right

def input_and_save(memory, oper, dest):
    inp = get_int()
    memory[dest] = inp

def output(memory, oper, src):
    if oper // 100 % 10 == 0:
        src = memory[src]
    print(src)

# This function is our intcode computer
# It executes the specified program and returns the output
def computer(program):
    # Start at position zero
    pos = 0

    # Copy the "program" into "memory"
    # Since it's a list, making changes to program will affect the one in caller too
    memory = program[:]

    while True:
        oper = memory[pos]
        opcode = oper % 100
        if opcode in [1,2]:
            add_or_mult(memory, *memory[pos:pos+4])
            pos += 4
        elif opcode == 3:
            input_and_save(memory, *memory[pos:pos+2])
            pos += 2
        elif opcode == 4:
            output(memory, *memory[pos:pos+2])
            pos += 2
        elif opcode == 99:
            break
        else:
            print(f'Error, invalid opcode: {opcode}', file=sys.stderr)
            exit(1)
    return memory[0]

def part_one():
    # The program instructions are stored as text
    # Read it in and convert to list of ints
    with open(input_file) as f:
        commands = list(map(lambda x: int(x), f.read().split(',')))
    
    return computer(commands)

def part_two():
    # The program instructions are stored as text
    # Read it in and convert to list of ints
    with open(input_file) as f:
        commands = list(map(lambda x: int(x), f.read().split(',')))

    # Replace noun and verb until program output matches program description
    for noun in range(100):
        for verb in range(100):
            commands[1] = noun
            commands[2] = verb
            if computer(commands) == 19690720:
                return 100 * noun + verb

part_one()
# print(part_two())


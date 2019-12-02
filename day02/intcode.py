input_file = 'input'
opcodes = [1, 2]

# This function is our intcode computer
# It executes the specified program and returns the output
def computer(program):
    # Start at position zero
    pos = 0

    # Copy the "program" into "memory"
    # Since it's a list, making changes to program will affect the one in caller too
    memory = program[:]

    while True:
        opcode = memory[pos]
        if opcode in opcodes:
            loc1, loc2, loc3 = memory[pos+1:pos+4]
            if opcode == 1:
                memory[loc3] = memory[loc1] + memory[loc2]
            elif opcode == 2:
                memory[loc3] = memory[loc1] * memory[loc2]
            pos += 4
        elif opcode == 99:
            break
        else:
            print("Error, invalid opcode")
            break
    return memory[0]

def part_one():
    # The program instructions are stored as text
    # Read it in and convert to list of ints
    with open(input_file) as f:
        commands = list(map(lambda x: int(x), f.read().split(',')))
    
    # Replace these two values as specified in program description
    commands[1] = 12
    commands[2] = 2
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

print(part_one())
print(part_two())


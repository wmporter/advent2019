import itertools

input_file = 'input'

# Addition and multiplication operations
# Opcodes 1 and 2
def add_or_mult(memory, oper, left, right, result):
    if oper // 100 % 10 == 0:
        left = memory[left]
    if oper // 1000 % 10 == 0:
        right = memory[right]
    if oper % 100 == 1:
        memory[result] = left + right
    else:
        memory[result] = left * right

# Modified from original
# Instead of getting input, the input is passed in
# Opcode 3
def input_and_save(inp, memory, oper, dest):
    memory[dest] = inp

# Read memory location and output
# Opcode 4
def output(memory, oper, src):
    if oper // 100 % 10 == 0:
        src = memory[src]
    print(src)

# Jump if true and jump if false operations
# Opcodes 5 and 6
def jmp_if_bool(memory, pos, oper, cond, dest):
    if oper // 100 % 10 == 0:
        cond = memory[cond]
    if oper // 1000 % 10 == 0:
        dest = memory[dest]
    # Opcode 5 is jump if true, opcode 6 is jump if false
    if (oper % 100 == 5 and cond) or (oper % 100 == 6 and not cond):
        return dest
    else:
        return pos + 3

# "Less than" and "equal to" operations
# Opcodes 7 and 8
def compare(memory, oper, left, right, dest):
    if oper // 100 % 10 == 0:
        left = memory[left]
    if oper // 1000 % 10 == 0:
        right = memory[right]
    if oper % 100 == 7 and left < right:
        memory[dest] = 1
    elif oper % 100 == 8 and left == right:
        memory[dest] = 1
    else:
        memory[dest] = 0

# This function is our advanced intcode computer
# It executes the specified program and returns the output
def computer_adv(phase, signal, program):
    # Start at position zero
    pos = 0

    # Copy the "program" into "memory"
    # Since it's a list, making changes to program will affect the one in caller too
    memory = program[:]

    # Save the inputs to a list in reverse order they are needed so we can use .pop()
    inputs = [signal, phase]
    while True:
        oper = memory[pos]
        opcode = oper % 100
        if opcode in [1,2]:
            add_or_mult(memory, *memory[pos:pos+4])
            pos += 4
        elif opcode == 3:
            # Modified from original
            # Pop value from inputs list and pass it in rather than getting actual input
            input_and_save(inputs.pop(), memory, *memory[pos:pos+2])
            pos += 2
        elif opcode == 4:
            # Modified from original
            # Just save the output instead of outputing it
            outp = memory[memory[pos+1]]
            pos += 2
        elif opcode in [5, 6]:
            pos = jmp_if_bool(memory, pos, *memory[pos:pos+3])
        elif opcode in [7, 8]:
            compare(memory, *memory[pos:pos+4])
            pos += 4
        elif opcode == 99:
            break
        else:
            print(f'Error, invalid opcode: {opcode}', file=sys.stderr)
            exit(1)
    # return memory[0]
    return outp

def part_one():
    # The program instructions are stored as text
    # Read it in and convert to list of ints
    with open(input_file) as f:
        commands = list(map(lambda x: int(x), f.read().split(',')))
    
    max_output = 0
    max_sequence = None
    for perm in itertools.permutations(range(5)):
        out_a = computer_adv(perm[0], 0, commands)
        out_b = computer_adv(perm[1], out_a, commands)
        out_c = computer_adv(perm[2], out_b, commands)
        out_d = computer_adv(perm[3], out_c, commands)
        out_e = computer_adv(perm[4], out_d, commands)
        if out_e > max_output:
            max_output = out_e
            max_sequence = perm
    return max_output, max_sequence

print(part_one())
const fs = require('fs');

const input_file = 'input';
const opcodes = [1, 2];

// This function is our intcode computer
// It executes the specified program and returns the output
function computer(program) {
    // Start at position zero
    let pos = 0;

    // Copy the "program" into "memory"
    // Since it's a list, making changes to program will affect the one in caller too
    memory = Array.from(program);

    while(true) {
        let opcode = memory[pos];
        if (opcodes.includes(opcode)) {
            let [loc1, loc2, loc3] = memory.slice(pos+1, pos+4);
            if (opcode === 1) memory[loc3] = memory[loc1] + memory[loc2];
            else if (opcode === 2) memory[loc3] = memory[loc1] * memory[loc2];
            pos += 4;
        }
        else if (opcode == 99) break;
        else {
            console.log("Error, invalid opcode");
            break;
        }
    }
    return memory[0];
}

function partOne() {
    // The program instructions are stored as text
    // Read it in and convert to list of ints 
    const commands = fs.readFileSync(input_file, { encoding: 'utf-8' })
        .split(',')
        .map(x => parseInt(x));
    
    // Replace these two values as specified in program description
    commands[1] = 12;
    commands[2] = 2;
    return computer(commands);
}

function partTwo() {
    // The program instructions are stored as text
    // Read it in and convert to list of ints 
    const commands = fs.readFileSync(input_file, { encoding: 'utf-8' })
        .split(',')
        .map(x => parseInt(x));

    // Replace noun and verb until program output matches program description
    for (let noun = 0; noun < 100; noun++) {
        for (let verb = 0; verb < 100; verb++) {
            commands[1] = noun;
            commands[2] = verb;
            if (computer(commands) === 19690720) 
                return 100 * noun + verb;
        }
    }
}

console.log(partOne())
console.log(partTwo())


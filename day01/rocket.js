var fs = require('fs');
const inputFile = 'input';

// Part One
function partOne() {
    let total_fuel = 0;
    // Use trim to avoid any extra newlines being parsed as NaN by parseInt
    // Create an array of the masses from the input file
    const masses = fs.readFileSync(inputFile, { encoding: 'utf-8' }).trim().split('\n');
    for (let i = 0; i < masses.length; i++) {
        total_fuel += Math.floor(parseInt(masses[i]) / 3) - 2;
    }
    return total_fuel;
}

// Part Two
function partTwo() {
    let total_fuel = 0;
    // Use trim to avoid any extra newlines being parsed as NaN by parseInt
    // Create an array of the masses from the input file
    const masses = fs.readFileSync(inputFile, { encoding: 'utf-8' }).trim().split('\n');
    for (let i = 0; i < masses.length; i++) {
        let fuel = Math.floor(parseInt(masses[i]) / 3) - 2;
        // Keep adding fuel until the fuel calculation is negative
        while(fuel > 0) {
            total_fuel += fuel;
            fuel = Math.floor(fuel / 3) - 2;
        }
    }
    return total_fuel;
}

console.log(partOne());
console.log(partTwo());
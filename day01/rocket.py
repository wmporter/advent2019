input_file = 'input'

# Part One
def part_one():
    total_fuel = 0
    with open(input_file) as f:
        # read a line and strip off the newline
        mass = f.readline().strip()
        while mass:
            # Integer division rounds down by definition
            total_fuel += int(mass) // 3 - 2
            mass = f.readline().strip()
    return total_fuel

# Part Two
def part_two():
    total_fuel = 0
    with open(input_file) as f:
        # read a line and strip off the newline
        mass = f.readline().strip()
        while mass:
            # Integer division rounds down by definition
            fuel = int(mass) // 3 - 2
            # Keep adding fuel until the fuel calculation is negative
            while fuel > 0:
                total_fuel += fuel
                fuel = fuel // 3 - 2
            mass = f.readline().strip()
    return total_fuel

print(part_one())
print(part_two())
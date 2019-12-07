input_file = 'input'

orbits = {
    'COM': {
        'parent': None,
        'children': [],
        'count': 0
    }
}

with open(input_file) as f:
    line = f.readline().strip()
    while line:
        parent, child = line.split(')')
        if parent in orbits:
            orbits[parent]['children'].append(child)
        else:
            orbits[parent] = {
                'children': [child]
            }
        if child in orbits:
            orbits[child]['parent'] = parent
        else:
            orbits[child] = {
                'parent': parent,
                'children': []
            }
        line = f.readline().strip()

def part_one():   
    total_orbits = 0
    # The list of planets yet to be processed
    # This list will be modified as we process the planets
    remaining = ['COM']
    while len(remaining) > 0:
        planet = remaining[0]
        orbit_count = orbits[planet]['count']
        # By looping over each planet's children, we are sure to visit every planet
        # once and only once because each planet is the child of exactly one parent planet
        for p in orbits[planet]['children']:
            orbits[p]['count'] = orbit_count + 1
            total_orbits += orbit_count + 1
        # Add all the children planets of the current planet to our list
        # And remove the current planet from it
        remaining.extend(orbits[planet]['children'])
        remaining = remaining[1:]

    return total_orbits

def part_two():
    # Create two lists that traces all the parents of each planet back to COM
    # Then find the first planet in common between the two and count the orbital transfers
    # to that common node using the indices of the lists
    you = 'YOU'
    san = 'SAN'
    you_trace = []
    san_trace = []
    
    next_parent = orbits[you]['parent']
    while next_parent:
        you_trace.append(next_parent)
        next_parent = orbits[next_parent]['parent']
    
    next_parent = orbits[san]['parent']
    while next_parent:
        san_trace.append(next_parent)
        next_parent = orbits[next_parent]['parent']
    
    for i, c in enumerate(you_trace):
        if c in san_trace:
            return i + san_trace.index(c)

print(part_one())
print(part_two())

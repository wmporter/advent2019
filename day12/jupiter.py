import re

def cmp(a, b):
    if a < b: return -1
    if a > b: return 1
    return 0

def gravity(moon1, moon2):
    x = cmp(moon1['pos'][0], moon2['pos'][0])
    y = cmp(moon1['pos'][1], moon2['pos'][1])
    z = cmp(moon1['pos'][2], moon2['pos'][2])
    moon1['vel'][0] -= x
    moon2['vel'][0] += x
    moon1['vel'][1] -= y
    moon2['vel'][1] += y
    moon1['vel'][2] -= z
    moon2['vel'][2] += z

def velocity(moon):
    moon['pos'][0] += moon['vel'][0]
    moon['pos'][1] += moon['vel'][1]
    moon['pos'][2] += moon['vel'][2]

def energy(moon):
    pot = sum(map(abs, moon['pos']))
    kin = sum(map(abs, moon['vel']))
    moon['energy'] = pot * kin

input_file = 'input'
line_regex = '^<x=([^ ]+), y=([^ ]+), z=([^ ]+)>$'
moons = []

with open(input_file) as f:
    line = f.readline()
    while(line):
        m = re.match(line_regex, line)
        x, y, z = map(lambda x: int(x), m.groups())
        moons.append({
            'pos': [x, y, z],
            'vel': [0, 0, 0],
            'energy': 0
        })
        line = f.readline()
for step in range(1000):
    for i in range(3):
        for j in range(i+1,4):
            gravity(moons[i], moons[j])

    for k in range(4):
        velocity(moons[k])
        energy(moons[k])
print(sum(map(lambda x: x['energy'], moons)))
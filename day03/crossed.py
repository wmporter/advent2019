input_file = 'input'
def manhattan(point):
    return abs(point[0]) + abs(point[1])

def segments(wire):
    horiz = []
    vert  = []
    pos = (0,0)
    for seg in wire:
        path = re.match('([UDLR])(\d+)', seg)
        dist = int(path.group(2))
        direction = path.group(1)
        if direction == 'U':
            newpos = (pos[0], pos[1] + dist)
            vert.append((pos, newpos))
        elif direction == 'D':
            newpos = (pos[0], pos[1] - dist)
            vert.append((pos, newpos))
        elif direction == 'L':
            newpos = (pos[0] - dist, pos[1])
            horiz.append((pos, newpos))
        elif direction == 'R':
            newpos = (pos[0] + dist, pos[1])
            horiz.append((pos, newpos))
        pos = newpos
    return horiz, vert

def intersect(vert, horiz):
    return (vert[0] in horiz or 
    vert[1] in horiz or
    (sorted([vert[0][1], vert[1][1], horiz[0][1]])[1] == horiz[0][1] and
    sorted([horiz[0][0], horiz[1][0], vert[0][0]])[1] == vert[0][0]))

with open(input_file) as f:
    wire1 = f.readline().split(',')
    wire2 = f.readline().split(',')

horiz1, vert1 = segments(wire1)
horiz2, vert2 = segments(wire2)
min_dist = 1_000_000_000
for h in horiz1:
    for v in vert2:
        if intersect(v, h):
            if (0,0) in v and (0,0) in h:
                pass
            else:
                if manhattan((v[0][0], h[0][1])) < min_dist:
                    min_dist = manhattan((v[0][0], h[0][1]))

for h in horiz2:
    for v in vert1:
        if intersect(v, h):
            if (0,0) in v and (0,0) in h:
                pass
            else:
                if manhattan((v[0][0], h[0][1])) < min_dist:
                    min_dist = manhattan((v[0][0], h[0][1]))

print(min_dist)
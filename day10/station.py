input_file = 'input'

# Every unique combination of angle (slope) and quadrant counts as visible
# but only once
def calc_visible(asteroid, asteroids):
    visible = []
    for a in asteroids:
        if asteroid == a:
            continue
        angle = ''
        if a[0] != asteroid[0] and a[1] != asteroid[1]:
            angle += str((a[1] - asteroid[1]) / (a[0] - asteroid[0]))
        if a[1] < asteroid[1]: angle += 'U'
        elif a[1] > asteroid[1]: angle += 'D'
        if a[0] < asteroid[0]: angle += 'L'
        elif a[0] > asteroid[0]: angle += 'R'
        if not angle in visible:
            visible.append(angle)
    return visible
        
def part_one():       
    # Read in input and make list of asteroid stations (based on location)
    asteroids = []
    row = 0
    with open(input_file) as f:
        line = f.readline()
        while(line):
            for col, a in enumerate(line):
                if a == '#':
                    asteroids.append((col, row))
            line = f.readline()
            row += 1

    # Iterate over every asteroid and count its visible asteroids, noting the maximum
    max_visible = 0
    for i, asteroid in enumerate(asteroids):
        visible = calc_visible(asteroid, asteroids)
        max_visible = max(max_visible, len(visible))
    return max_visible

print(part_one())
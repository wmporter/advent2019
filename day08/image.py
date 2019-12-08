w = 25
h = 6
size = w * h
with open('input') as f:
    image = f.read().strip()

def part_one():
    zero_digs = []
    one_two_digs = []
    layer = 0

    while True:
        if layer * size >= len(image):
            break
        zeroes, ones, twos = (0, 0, 0)
        for i in range(size):
            pixel = image[layer * size + i]
            if pixel == '0':
                zeroes += 1
            if pixel == '1':
                ones += 1
            if pixel == '2':
                twos += 1
        zero_digs.append(zeroes)
        one_two_digs.append(ones * twos)
        layer += 1
    return one_two_digs[zero_digs.index(min(zero_digs))]

def part_two():
    layer = 0
    result = ['?' for x in range(size)]

    while True:
        if layer * size >= len(image):
            break
        for i in range(size):
            pixel = image[layer * size + i]
            if pixel == '0' and result[i] == '?':
                result[i] = 'X'
            if pixel == '1' and result[i] == '?':
                result[i] = ' '
        layer += 1
    return '\n'.join([''.join(result[w*i:w*i+w]) for i in range(h)])

print(part_one())
print(part_two())

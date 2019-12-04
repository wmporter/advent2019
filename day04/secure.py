input_min = 145852
input_max = 616942

def valid_password(s):
    adjacent_pair = False
    for c in range(5):
        if int(s[c]) > int(s[c+1]): 
            return False 
        elif s[c] == s[c+1]:
            adjacent_pair = True
    return adjacent_pair

def valid_password2(s):
    adjacent_pair = False
    for c in range(5):
        if int(s[c]) > int(s[c+1]): 
            return False 
        elif s[c] == s[c+1]:
            left_good = (c == 0 or s[c] != s[c-1])
            right_good = (c == 4 or s[c+1] != s[c+2])
            if left_good and right_good:
                adjacent_pair = True
    return adjacent_pair

def part_one():
    pass_count = 0
    for i in range(input_min, input_max+1):
        j = str(i)
        if valid_password(j):
            pass_count += 1
    return pass_count

def part_two():
    pass_count = 0
    for i in range(input_min, input_max+1):
        j = str(i)
        if valid_password2(j):
            pass_count += 1
    return pass_count

print(part_one())
print(part_two())

input_file = open('input.txt', 'r')
lines = input_file.readlines()
     

def part_one():
    top = 0
    current = 0

    for line in lines:
        if line.strip() == '':
            if current > top:
                top = current
            current = 0
        else:
            current += int(line.strip())

    print(top) 

def part_two():
    top = [0, 0, 0]
    current = 0
 
    for line in lines:
        if line.strip() == '':
            compare_and_replace_top(current, top)
            current = 0
        else:
            current += int(line.strip())

    print(sum(top))

def compare_and_replace_top(value, top):
    if value > top[0]:
        compare_and_replace_top(top[0], top)
        top[0] = value
    elif value > top[1]:
        compare_and_replace_top(top[1], top)
        top[1] = value
    elif value > top[2]:
        compare_and_replace_top(top[2], top)
        top[2] = value

part_two()
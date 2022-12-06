
def read_stacks(lines):
    number_of_stacks = int(len(lines[0]) / 4)
    print('Number of stacks: ' + str(number_of_stacks))

    stacks = []
    for i in range(number_of_stacks):
        stacks.append([])

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.strip() == '':
            break

        if '[' in stripped_line:
            for i in range(number_of_stacks):
                stack_item = line[i*4:i*4+4].replace('[', '').replace(']', '').strip()
                if stack_item != '':
                    print(stack_item)
                    stacks[i].append(stack_item)

    for i in range(number_of_stacks):
        stacks[i].reverse()

    print(stacks)
    return stacks

def execute_move(stacks, move):
    move_glyphs = move.split(' ')

    amount = int(move_glyphs[1])
    source = int(move_glyphs[3])-1
    target = int(move_glyphs[5])-1

    for i in range(amount):
        if stacks[source]:
            item = stacks[source].pop()
            stacks[target].append(item)

def part_one():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    stacks = read_stacks(lines)

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('move'):
            execute_move(stacks, stripped_line)

    top_items = ''
    for i in range(len(stacks)):
        top_items += stacks[i][-1]

    print('part one: ' + str(top_items))

part_one()
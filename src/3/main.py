
priority_table = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

def get_priority_value(item):
    priority = priority_table[item.lower()]
    if item.isupper():
        return priority + 26
    else:
        return priority

def parse_rucksack(rucksack):
    first_compartment  = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]

    for index in range(0, len(first_compartment)):
        if first_compartment[index] in second_compartment:
            return get_priority_value(first_compartment[index])

    return 0

def parse_rucksack_group(rucksack_group):

    for index in range(0, len(rucksack_group[0])):
        if rucksack_group[0][index] in rucksack_group[1] and rucksack_group[0][index] in rucksack_group[2]:
            return get_priority_value(rucksack_group[0][index])

    return 0

def part_one():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    total_priority = 0

    for line in lines:
        priority = parse_rucksack(line.strip())
        total_priority += priority

    print('part one: ' + str(total_priority))

def part_two():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    total_priority = 0
    rucksack_count = 0
    rucksacks_to_parse = ['', '', '']

    for line in lines:
        rucksacks_to_parse[rucksack_count] = line.strip()
        rucksack_count += 1

        if rucksack_count == 3:
            priority = parse_rucksack_group(rucksacks_to_parse)
            total_priority += priority
            rucksack_count = 0

    print('part two: ' + str(total_priority))

part_one()
part_two()
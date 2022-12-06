
def parse_pair(pair):
    sections = pair.split(',')
    section1 = sections[0].split('-')
    section2 = sections[1].split('-')

    section1_start = int(section1[0])
    section1_end = int(section1[1])

    section2_start = int(section2[0])
    section2_end = int(section2[1])

    if section1_start <= section2_start and section1_end >= section2_end:
        return True
    if section2_start <= section1_start and section2_end >= section1_end:
        return True

    return False

def parse_pair_two(pair):
    sections = pair.split(',')
    section1 = sections[0].split('-')
    section2 = sections[1].split('-')

    section1_start = int(section1[0])
    section1_end = int(section1[1])

    section2_start = int(section2[0])
    section2_end = int(section2[1])

    if (section1_start <= section2_start and section1_end >= section2_start 
        or section1_start <= section2_end and section1_end >= section2_end
        or section2_start <= section1_start and section2_end >= section1_start
        or section2_start <= section1_end and section2_end >= section1_end):
        return True

    return False

def part_one():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    contained_pairs = 0

    for line in lines:
        pair_contained = parse_pair(line)

        if (pair_contained):
            contained_pairs += 1

    print('part one: ' + str(contained_pairs))

def part_two():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    contained_pairs = 0

    for line in lines:
        pair_contained = parse_pair_two(line)

        if (pair_contained):
            contained_pairs += 1

    print('part two: ' + str(contained_pairs))

part_one()
part_two()

x = 1
current_tick = 1
targets = [20, 60, 100, 140, 180, 220]
signals = []

def handle_command(command):
    global current_tick, x, targets, signals

    current_tick += 1

    if current_tick in targets:
        signals.append(current_tick * x)

    if command.startswith('addx'):
        current_tick += 1
        x += int(command.split(' ')[1])

        if current_tick in targets:
            signals.append(current_tick * x)

def part_one():
    input_file = open('Z:\\dev\\aoc22\\src\\10\\input.txt', 'r')
    lines = input_file.readlines()

    for line in lines:
        handle_command(line.strip())

    print(signals)
    print('part one: ' + str(sum(signals)))

part_one()
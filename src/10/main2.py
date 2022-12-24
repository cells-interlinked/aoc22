
x = 1
current_tick = 0
crt_position = 0
screen_buffer = []

def handle_command(command):
    global current_tick, x, targets, signals

    current_tick += 1

    draw()

    if command.startswith('addx'):
        current_tick += 1
        draw()
        x += int(command.split(' ')[1])

def draw():
    global crt_position, x, screen_buffer
    if crt_position == x or crt_position == x-1 or crt_position == x+1:
        screen_buffer.append('#')
    else:
        screen_buffer.append(".")
    crt_position += 1
    if crt_position == 40:
        crt_position = 0

def main():
    input_file = open('Z:\\dev\\aoc22\\src\\10\\input.txt', 'r')
    lines = input_file.readlines()

    for line in lines:
        handle_command(line.strip())

    write_buffer = ''
    for i in range(len(screen_buffer)):
        write_buffer += screen_buffer[i]
        if (i+1) % 40 == 0 and i != 0:
            print(write_buffer)
            write_buffer = ''

main()

def part_one():
    input_file = open('input.txt', 'r')
    buffer = input_file.read()

    packet_start = 0
    read_buffer = []
    for i in range(len(buffer)):
        if len(read_buffer) == 4:
            read_buffer.pop(0)
        read_buffer.append(buffer[i])

        if len(read_buffer) == 4:
            read_set = set(read_buffer)
            if len(read_set) == len(read_buffer):
                print(read_set)
                print(read_buffer)
                packet_start = i + 1
                break

    print('part one: ' + str(packet_start))

part_one()
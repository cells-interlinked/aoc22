
def determine_visible(x, y, grid, width, height):
    cell_height = grid[y][x]
    
    if x == 0 or y == 0:
        return True
    if x == width-1 or y == height-1:
        return True

    left = True
    right = True
    up = True
    down = True

    #right
    for i in range(x+1, width):
        target_height = grid[y][i]
        if target_height >= cell_height:
            right = False
            break
    #left
    for i in range(0, x):
        target_height = grid[y][i]
        if target_height >= cell_height:
            left = False
            break
    #up
    for i in range(0, y):
        target_height = grid[i][x]
        if target_height >= cell_height:
            up = False
            break
    #down
    for i in range(y+1, height):
        target_height = grid[i][x]
        if target_height >= cell_height:
            down = False
            break

    return left or right or up or down

def part_one():
    input_file = open('Z:\\dev\\aoc22\\src\\8\\input.txt', 'r')
    lines = input_file.readlines()

    width = len(lines[0].strip())
    height = len(lines)
    print('width: ' + str(width) + ' height: ' + str(height))

    visible_cells = 0

    grid = []

    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(int(lines[i].strip()[j]))

    for i in range(height):
        row = ''
        for j in range(width):
            visible = determine_visible(j, i, grid, width, height)
            if visible:
                row += str(grid[i][j])
                visible_cells += 1
            else:
                row += 'x'
        print(row)

    print('part one: ' + str(visible_cells))

part_one()
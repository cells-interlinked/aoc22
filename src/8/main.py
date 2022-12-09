
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

def determine_scenic(x, y, grid, width, height):
    cell_height = grid[y][x]
    
    left = 0
    right = 0
    up = 0
    down = 0

    view_distance = 0
    #right
    for i in range(x+1, width):
        view_distance += 1
        target_height = grid[y][i]
        if target_height >= cell_height:
            break
    right = view_distance
    view_distance = 0
    #left
    for i in range(x-1, -1, -1):
        view_distance += 1
        target_height = grid[y][i]
        if target_height >= cell_height:
            break
    left = view_distance
    view_distance = 0
    #up
    for i in range(y-1, -1, -1):
        view_distance += 1
        target_height = grid[i][x]
        if target_height >= cell_height:
            break
    up = view_distance
    view_distance = 0
    #down
    for i in range(y+1, height):
        view_distance += 1
        target_height = grid[i][x]
        if target_height >= cell_height:
            break
    down = view_distance
    return left * right * up * down

def part_two():
    input_file = open('Z:\\dev\\aoc22\\src\\8\\input.txt', 'r')
    lines = input_file.readlines()

    width = len(lines[0].strip())
    height = len(lines)
    print('width: ' + str(width) + ' height: ' + str(height))

    top_score = 0

    grid = []

    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(int(lines[i].strip()[j]))

    for i in range(height):
        row = ''
        for j in range(width):
            scenic_score = determine_scenic(j, i, grid, width, height)
            row += str(scenic_score)
            if scenic_score > top_score:
                top_score = scenic_score
                
        print(row)

    print('part two: ' + str(top_score))

#part_one()
part_two()
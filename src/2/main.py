
rock = 'rock'
paper = 'paper'
scissors = 'scissors'

def decrypt_move(value):
    if value == 'A' or value == 'X':
        return rock
    if value == 'B' or value == 'Y':
        return paper
    if value == 'C' or value == 'Z':
        return scissors

def determine_needed_move(key, opponent):
    if key == 'X': # lose
        if opponent == rock:
            return scissors
        elif opponent == paper:
            return rock
        elif opponent == scissors:
            return paper
    if key == 'Y': # draw
        return opponent
    if key == 'Z': # win
        if opponent == rock:
            return paper
        elif opponent == paper:
            return scissors
        elif opponent == scissors:
            return rock

def handle_match(me, opponent):
    match_points = 0

    if me == rock:
        match_points += 1
    if me == paper:
        match_points += 2
    if me == scissors:
        match_points += 3

    match_points += determine_win(me, opponent)
    return match_points

def determine_win(me, opponent):
    if me == opponent:
        return 3
    elif me == rock and opponent == scissors:
        return 6
    elif me == paper and opponent == rock:
        return 6
    elif me == scissors and opponent == paper:
        return 6

    return 0

def part_one():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    score = 0

    for line in lines:
        moves = line.strip().split(' ')
        opponent = decrypt_move(moves[0])
        me = decrypt_move(moves[1])

        match_points = handle_match(me, opponent)
        score += match_points

    print('part one:' + str(score))

def part_two():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    score = 0

    for line in lines:
        moves = line.strip().split(' ')
        opponent = decrypt_move(moves[0])
        me = determine_needed_move(moves[1], opponent)

        match_points = handle_match(me, opponent)
        score += match_points

    print('part two:' + str(score))

part_one()
part_two()
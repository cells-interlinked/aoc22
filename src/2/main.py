
def decrypt_key(value):
    if value == 'A' or value == 'X':
        return 'rock'
    if value == 'B' or value == 'Y':
        return 'paper'
    if value == 'C' or value == 'Z':
        return 'scissors'

def handle_match(me, opponent):
    match_points = 0

    if me == 'rock':
        match_points += 1
    if me == 'paper':
        match_points += 2
    if me == 'scissors':
        match_points += 3

    match_points += determine_win(me, opponent)
    return match_points

def determine_win(me, opponent):
    if me == opponent:
        return 3
    elif me == 'rock' and opponent == 'scissors':
        return 6
    elif me == 'paper' and opponent == 'rock':
        return 6
    elif me == 'scissors' and opponent == 'paper':
        return 6

    return 0

def part_one():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    score = 0

    for line in lines:
        moves = line.strip().split(' ')
        opponent = decrypt_key(moves[0])
        me = decrypt_key(moves[1])

        match_points = handle_match(me, opponent)
        score += match_points

    print(score)

part_one()
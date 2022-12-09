
import math
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.x == other.x and self.y == other.y

class Rope:
    def __init__(self):
        self.head_pos = Vec2(0, 0)
        self.head_prev_pos = Vec2(0, 0)
        self.tail_pos = Vec2(0, 0)

        self.visited_pos = set()
        self.visited_pos.add(Vec2(0, 0))

    def apply_move(self, x, y):
        self.head_prev_pos.x = self.head_pos.x 
        self.head_prev_pos.y = self.head_pos.y

        self.head_pos.x += x
        self.head_pos.y += y

        if vector_distance(self.head_pos, self.tail_pos) > 1.5:
            self.tail_pos.x = self.head_prev_pos.x
            self.tail_pos.y = self.head_prev_pos.y
            self.visited_pos.add(Vec2(self.tail_pos.x, self.tail_pos.y))

class Move:
    def __init__(self, dir, dist):
        self.dir = dir
        self.dist = dist

def move_rope(rope, move):
    for i in range(move.dist):
        if move.dir == 'U':
            rope.apply_move(0, 1)
        if move.dir == 'D':
            rope.apply_move(0, -1)
        if move.dir == 'L':
            rope.apply_move(-1, 0)
        if move.dir == 'R':
            rope.apply_move(1, 0)

def vector_distance(vec1, vec2):
    return math.sqrt(pow(vec1.x-vec2.x, 2) + pow(vec1.y-vec2.y, 2))

def part_one():
    input_file = open('Z:\\dev\\aoc22\\src\\9\\input.txt', 'r')
    lines = input_file.readlines()

    rope = Rope()

    for line in lines:
        parsed_line = line.strip().split(' ')
        move = Move(parsed_line[0], int(parsed_line[1]))

        move_rope(rope, move)

    print('part one: ' + str(len(rope.visited_pos)))

part_one()
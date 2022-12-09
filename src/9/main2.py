
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
        self.head = Node(None, None)
        for i in range(9):
            self.head.add_node()

        self.visited_pos = set()
        self.visited_pos.add(Vec2(0, 0))

    def apply_move(self, x, y):
        self.head.apply_move(x, y, self.visited_pos)

class Node:
    def __init__(self, last, next):
        self.pos = Vec2(0,0)
        self.prev_pos = Vec2(0, 0)
        self.last = last
        self.next = next

    def add_node(self):
        if self.next == None:
            self.next = Node(self, None)
        else:
            self.next.add_node()

    def apply_move(self, x, y, visited_pos):
        self.prev_pos.x = self.pos.x 
        self.prev_pos.y = self.pos.y

        self.pos.x += x
        self.pos.y += y

        if self.next != None:
            self.next.update(visited_pos)

    def update(self, visited_pos):
        if vector_distance(self.pos, self.last.pos) > 1.5:
            self.prev_pos.x = self.pos.x
            self.prev_pos.y = self.pos.y

            #self.pos.x = self.last.prev_pos.x
            #self.pos.y = self.last.prev_pos.y

            if self.last.pos.x > self.pos.x:
                self.pos.x += 1
            if self.last.pos.x < self.pos.x:
                self.pos.x -= 1

            if self.last.pos.y > self.pos.y:
                self.pos.y += 1
            if self.last.pos.y < self.pos.y:
                self.pos.y -= 1

            if self.next != None:
                self.next.update(visited_pos)
            else:
                visited_pos.add(Vec2(self.pos.x, self.pos.y))



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

def part_two():
    input_file = open('Z:\\dev\\aoc22\\src\\9\\input.txt', 'r')
    lines = input_file.readlines()

    rope = Rope()

    for line in lines:
        parsed_line = line.strip().split(' ')
        move = Move(parsed_line[0], int(parsed_line[1]))

        move_rope(rope, move)

    print('part two: ' + str(len(rope.visited_pos)))

part_two()
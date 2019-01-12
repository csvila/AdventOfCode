# from utils.decorators import time_it

with open('input13.txt') as f:
    puzzle_input = f.readlines()


class Cart:
    def __init__(self, id, pos, sym):
        self.id = id
        self.pos = pos

        # 0 = North
        # 1 = East
        # 2 = South
        # 3 = West
        if sym == '^':
            self.dir = 0
        elif sym == '>':
            self.dir = 1
        elif sym == 'v':
            self.dir = 2
        elif sym == '<':
            self.dir = 3

        self.turn = 0
        self.dead = False

    def move(self, track):

        if self.dir == 0:
            self.pos[0] -= 1  # Move north
        elif self.dir == 1:
            self.pos[1] += 1  # Move east
        elif self.dir == 2:
            self.pos[0] += 1  # Move south
        elif self.dir == 3:
            self.pos[1] -= 1  # Move west

        x, y = self.pos
        curr_track = track[x][y]
        if curr_track in '/\\':
            if self.dir == 1 or self.dir == 3:
                if curr_track == '\\':
                    self.dir += 1
                else:
                    self.dir -= 1
            elif self.dir == 0 or self.dir == 2:
                if curr_track == '/':
                    self.dir += 1
                else:
                    self.dir -= 1
        elif curr_track == '+':
            if self.turn == 0:
                self.dir -= 1
            elif self.turn == 2:
                self.dir += 1
            self.turn += 1
            self.turn %= 3
        elif curr_track in '|-':
            pass
        else:
            print('invalid track')
        self.dir %= 4

    def __eq__(self, other):
        return self.pos == other.pos


# @time_it
def part_one(n):
    paths = [[c for c in line.strip('\n')] for line in n]
    carts = []
    id = 0
    for i, line in enumerate(paths):
        for j, spot in enumerate(line):
            if spot in '^>v<':
                carts.append(Cart(id, [i, j], spot))
                id += 1
            if spot in '^v':
                paths[i][j] = '|'
            elif spot in '<>':
                paths[i][j] = '-'

    collision = False
    while not collision:
        carts = sorted(carts, key=lambda c: (c.pos[0], c.pos[1]))
        for i, cart in enumerate(carts):
            if cart.dead:
                collision = True
                break
            if not cart.dead:
                cart.move(paths)
            for other in carts[:i] + carts[i + 1:]:
                if cart == other:
                    cart.dead = True
                    other.dead = True
                    break
    y, x = carts[0].pos
    return x, y


# @time_it
def part_two(n):
    paths = [[c for c in line.strip('\n')] for line in n]
    carts = []
    id = 0
    for i, line in enumerate(paths):
        for j, spot in enumerate(line):
            if spot in '^>v<':
                carts.append(Cart(id, [i, j], spot))
                id += 1
            if spot in '^v':
                paths[i][j] = '|'
            elif spot in '<>':
                paths[i][j] = '-'

    collision = False
    while not collision:
        carts = sorted(carts, key=lambda c: (c.pos[0], c.pos[1]))
        for i, cart in enumerate(carts):
            cart.move(paths)
            for other in carts[:i]+carts[i+1:]:
                if not (cart.dead or other.dead) and cart == other:
                    cart.dead = True
                    other.dead = True
        if len([x for x in carts if not x.dead]) == 1:
            break

    temps = {}
    for cart in carts:
        if not cart.dead:
            x, y = cart.pos
            temps[(x, y)] = paths[x][y]
            paths[x][y] = str(cart.id)
    for line in paths:
        print(''.join(line))

    for (x, y), v in temps.items():
        paths[x][y] = v

    for cart in carts:
        if not cart.dead:
            y, x = cart.pos
    return x, y


test_input = [
    '/->-\\        ',
    '|   |  /----\\',
    '| /-+--+-\  |',
    '| | |  | v  |',
    '\-+-/  \-+--/',
    '  \------/   '
]

test_two = [
    '/>-<\\  ',
    '|   |  ',
    '| /<+-\\',
    '| | | v',
    '\>+</ |',
    '  |   ^',
    '  \<->/'
]

p1 = part_one(test_input)
# print(p1)
assert p1 == (7, 3)

p2 = part_two(test_two)
# print(p2)
assert p2 == (6, 4)

print(f'Part 1: {part_one(puzzle_input)}')
print(f'Part 2: {part_two(puzzle_input)}')

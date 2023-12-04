import os

folder = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(folder, 'input.txt')

def main():
    games = [] # look at index+1 to get the game's id
    with open(filepath, "r") as f:
        for line in f:
            games.append(parse_line(line))
    part_1(games)
    part_2(games)


class rgb:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def leq(self, other) -> bool:
        return self.r <= other.r and self.g <= other.g and self.b <= other.b
    
    def power(self) -> int:
        return self.r * self.g * self.b

    def max(self, other):
        self.r = max(self.r, other.r)
        self.g = max(self.g, other.g)
        self.b = max(self.b, other.b)


def parse_line(line) -> [rgb]:
    result = []
    [_, rest] = line.strip().split(": ")
    sets = rest.split("; ")
    for set in sets:
        info = rgb(0, 0, 0)
        colors = set.split(", ")
        for color in colors:
            [num, name] = color.split(" ")
            if (name == "red"):
                info.r = int(num)
            elif (name == "green"):
                info.g = int(num)
            elif (name == "blue"):
                info.b = int(num)
        result.append(info)
    # print(sets)
    return result


def part_1(games: [[rgb]]):
    limit = rgb(12, 13, 14)
    sum = 0
    for i, game in enumerate(games):
        fits = True
        for set in game:
            if(not set.leq(limit)):
                fits = False
                break
        if fits:
            sum += i+1
    print("part 1:", sum)


def part_2(games: [[rgb]]):
    sum = 0
    for i, game in enumerate(games):
        minimum = rgb(0, 0, 0)
        for set in game:
            minimum.max(set)

        sum += minimum.power()
    print("part 2:", sum)


if __name__ == "__main__":
    main()

from collections import deque, defaultdict
import re


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


file = open('input09.txt').read()
players, max_marble = map(int, re.findall(r'\d+', file))

print(f'Part 1: {play_game(players, max_marble)}')
print(f'Part 2: {play_game(players, max_marble * 100)}')

from collections import defaultdict

words = []
C = defaultdict(int)

# #1 @ 604,100: 17x27


def read_lines():
    for line in open('input03.txt'):
        words.append(line.split())


def split_word(word):
    x, y = word[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = word[3].split('x')
    w, h = int(w), int(h)
    return x, y, w, h


def fill_dict():
    for word in words:
        x, y, w, h = split_word(word)
        for dx in range(w):
            for dy in range(h):
                C[(x + dx, y + dy)] += 1


def looking_not_overlap():
    for word in words:
        x, y, w, h = split_word(word)
        ok = True
        for dx in range(w):
            for dy in range(h):
                if C[(x + dx, y + dy)] > 1:
                    ok = False
        if ok:
            print(word[0])


read_lines()
fill_dict()
looking_not_overlap()

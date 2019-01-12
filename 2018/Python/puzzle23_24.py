'''
def nextg(cur, recipe):
  start = min(cur)
  end = max(cur)
  x = set()


  for i in range(start - 3, end + 4):
    pat = ''.join('#' if i + k in cur else '.' for k in [-2, -1, 0, 1, 2])
    if pat in recipe:
      x.add(i)

  return x


def viz(cur):
  print(''.join('#' if i in cur else '.' for i in range(-5, 120)))


with open('input12.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    print(lines)

    init = lines[0][len('initial state: '):]
    recipe = set()
    for l in lines[2:]:
        if l[-1] == '#':  # I forgot this line the first time around.
            recipe.add(l[:5])

    cur = set(i for i, c in enumerate(init) if c == '#')

    # Part 1:
    # for i in range(20):
    #    cur = nextg(cur, recipe)
    # print(f'1: {sum(cur)}')

    # Part 2:
    ls = 0
    # viz(cur)
    for i in range(50000000000):
        cur = nextg(cur, recipe)
        # viz(cur)
        s = sum(cur)
        # print(i, s, s - ls)
        ls = s
    print(f'2: {sum(cur)}')
#######################################################################
import parse

with open('input12.txt') as f:
    ls = [s.strip() for s in f.readlines()]

init_state = "####....#...######.###.#...##....#.###.#.###.......###.##..##........##..#.#.#..##.##...####.#..##.#"

rules = {}

pr = parse.compile("{} => {}")

for l in ls:
    r = pr.parse(l)
    rules[r[0]] = r[1]


def sum_plants(param_curr):
    internal_diff = (len(param_curr) - 100) // 2
    internal_sum = 0
    for i, c in enumerate(param_curr):
        if c == '#':
            internal_sum += (i - internal_diff)
    return internal_sum


curr = init_state
prev_sum = sum_plants(init_state)
diffs = []
num_iters = 1000
for i in range(num_iters):
    if i == 20:
        print("Part 1: " + str(sum_plants(curr)))
    curr = "...." + curr + "...."
    internal_next = ""
    for x in range(2, len(curr) - 2):
        sub = curr[x - 2:x + 3]
        internal_next += rules[sub]
    curr = internal_next
    currsum = sum_plants(curr)
    diff = currsum - prev_sum
    diffs.append(diff)
    if len(diffs) > 100:
        diffs.pop(0)
    prev_sum = currsum

last100diff = sum(diffs) // len(diffs)

total = (50000000000 - num_iters) * last100diff + sum_plants(curr)

print("Part 2: " + str(total))
'''

import re
import collections


def main(text, simple):
    if simple:
        return

    initial, *pairs = re.findall(r'[.#]+', text)
    mapping = {a: b for a, b in zip(pairs[::2], pairs[1::2])}

    pots = collections.defaultdict(lambda: '.')
    pots.update({i: v for i, v in enumerate(initial)})

    seen = {}
    for n in range(1, 1000):
        span = range(min(pots) - 5, max(pots) + 5)
        new = {
            i: mapping.get(window, '.')
            for i in span
            for window in [''.join(pots[i+j] for j in range(-2, 3))]
        }
        pots.clear()
        pots.update(new)

        if n == 19:
            print(sum(i for i, v in pots.items() if v == '#'))

        pattern = ''.join(pots[i] for i in span).strip('.')
        if pattern in seen:
            N = 50000000000
            x = sum(N + i - n for i, v in pots.items() if v == '#')
            print(x)
            break
        seen[pattern] = n


main(open('input12.txt').read(), False)

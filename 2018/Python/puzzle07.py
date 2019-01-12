from collections import defaultdict

lines = open('input04.txt').read().split('\n')
lines.sort()


def parse_time_of_line(line_data):
    word = line_data.split()
    date, time_clock = word[0][1:], word[1][:-1]
    return int(time_clock.split(':')[1])


def find_max_value(dic):
    best = None
    for k, v in dic.items():
        if best is None or v > dic[best]:
            best = k
    return best


C = defaultdict(int)
CM = defaultdict(lambda: defaultdict(int))
guard = None
asleep = None

for line in lines:
    if line:
        time = parse_time_of_line(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line:
            asleep = time
        elif 'wakes up' in line:
            for sleep in range(asleep, time):
                CM[guard][sleep] += 1
                C[guard] += 1

best_guard = find_max_value(C)
best_min = find_max_value(CM[best_guard])
print(best_guard, best_min)
print(best_guard * best_min)
lines = open('input05.txt').read().strip()

PolarityTable = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    PolarityTable[letter.lower()] = letter.upper()
    PolarityTable[letter.upper()] = letter.lower()

answer = 1e5

for remaining in alphabet:
    l2 = [c for c in lines if c != remaining.lower() and c != remaining.upper()]
    stack = []
    for c in l2:
        if stack and c == PolarityTable[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)
    answer = min(answer, len(stack))

print(answer)

lines = open('input05.txt').read().strip()

PolarityTable = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    PolarityTable[letter.lower()] = letter.upper()
    PolarityTable[letter.upper()] = letter.lower()

stack = []
for c in lines:
    if stack and c == PolarityTable[stack[-1]]:
        stack.pop()
    else:
        stack.append(c)

print(stack)
print(len(stack))

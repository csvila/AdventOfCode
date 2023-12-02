import os

folder = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(folder, 'input.txt')
lines=[]

with open(filepath, 'r') as f:
    for line in f.readlines():
        lines.append(line.strip())
sum=0

for l in lines:
    numeric_characters = [char for char in l if char.isdigit()]
    result = ''.join(numeric_characters)
    if len(result)==1:
        result = str(result)+str(result)
    val1=str(result[0])
    val2=str(result[-1])
    sum = sum + int(val1+val2)
print(sum)
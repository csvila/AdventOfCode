'''
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given
the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and
 fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing
character from either ID, producing fgij.)
'''

dic_letters = {}
ids = []
char_group = []
count2 = 0
count3 = 0


def load_data():
    f = open('input02.txt')
    line = f.readline()
    while line:
        ids.append(line.strip())
        # use readline() to read next line
        line = f.readline()
    f.close()


load_data()
for x in ids:
    for y in ids:
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                diff += 1
        if diff == 1:
            ans = []
            for i in range(len(x)):
                if x[i] == y[i]:
                    ans.append(x[i])
            print(''.join(ans))
            print(x, y)



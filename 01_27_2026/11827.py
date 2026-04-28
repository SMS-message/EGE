from itertools import product

REPEAT: int = 7
STRING: str | set = '01234567'

count = 0
for i in product(STRING, repeat=REPEAT):
    if i[0] != '0':
        even = [0 for j in i if int(j) % 2 == 0]
        sl = [h + '7' for h in '1357'] + ['7' + h for h in '1357']
        if len(even) == 2 and not any(x in i for x in sl):
            count += 1

print(count)

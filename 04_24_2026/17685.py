import re

with open("24_17685.txt") as f:
    s = f.read().strip()

st = set()

for i in range(len(s)):
    print(i, len(s))
    st |= set(re.findall(r"(?:\d+[+*])+\d+", s[i:i + 200]))

f = tuple(filter(lambda x: '00' not in x, st))
lst = []

for i in f:
    try:
        if eval(i) == 0:
            lst.append(i)
    except SyntaxError:
        continue

ans = max(lst, key=len)
print(len(ans), ans)

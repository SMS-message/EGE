import re

with open("24_28007.txt") as f:
    s = f.read().strip()

lst = re.findall(r"(?:\([1-9]\d+[12346789][+-][1-9][0-9]\d+[05]\))+", s)
print(max(map(len, lst)))

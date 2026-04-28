import re

with open("24_19149.txt") as f:
    s = f.read().strip()


lst = re.findall(r"\((?:\d+\+)+\d+\)", s)
lst = list(filter(lambda x: eval(x) % 2 == 0, lst))
print(max(map(len, lst)))
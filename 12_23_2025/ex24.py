import re

with open("24_25361.txt") as f:
    s = f.read().strip()


reg = r"[02468]"

lens = []

for string in re.split(reg, s)[1:]:
    if string.count("F") < 76:
        continue
    if string.count("F") == 76:
        lens.append(len(string) + 1)
    if string.count("F") > 76:
        split = string.split("F")
        lens.append(sum(tuple(map(len, split))[:77]) + 76 + 1)

print(max(lens))
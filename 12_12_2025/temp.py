import re


def check(line: str):
    digits = re.split(r"[+*]", line)
    c = line.count("+") + line.count("*")
    if len(digits) + c > 40:
        return False
    return True


with open("24_24895.txt") as file:
    s = file.read().strip()

reg = r"\d+(?:[*+]\d+)+"

findall = re.findall(reg, s)
res = filter(check, findall)

print(max(map(len, res)))

"""

"""
import re

with open("24_26549.txt") as f:
    s = f.read().strip()

s = re.split(r"2025", s)

lens = []

for i in range(50, len(s)):
    win = s[i - 50:i]

    if sum(map(lambda x: x.count("Y"), win)) >= 140:
        lens.append([50 * 4 + 3 + sum(map(len, win)), '025' + '2025'.join(win) + '2025'])

print(max(lens))


"""
№ 29354 Открытый вариант 2026 (Уровень: Базовый)
"""

import re

with open("24_29354.txt") as f:
    s = f.read().strip()

split = re.split(r"BC", s)

max_len = 0

for i in range(len(split) - 191):
    win = "BC".join(split[i:i + 191])
    max_len = max(max_len, len(win) + 2 if i != 0 and i != len(split) - 191 else 1)

print(max_len)

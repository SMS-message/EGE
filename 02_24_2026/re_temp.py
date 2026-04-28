"""
https://education.yandex.ru/ege/inf/task/60136ef5-552a-4bc0-9224-2914e321d93b
"""

import re

with open("24.txt") as f:
    s = f.readline().strip()

    print(re.findall(r"[1-9]\d+(?:[*-][1-9]\d+)+", s))

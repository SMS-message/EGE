"""
№ 28007 (Уровень: Средний)
"""

with open("24_28005.txt") as f:
    s = f.read().strip().lower()

s = s.split("@")

lst = []

for i, ss in enumerate(s[1:], 1):
    if i == len(s):
        break
    for server in "yandex.ru", "gmail.com":
        try:
            if ss.startswith(server):
                if ".." not in s[i - 1] and s[i - 1][-1] != '.':
                    lst.append(s[i - 1] + "@" + server)
        except IndexError:
            ...

max_by_len = max(lst, key=len)
print(len(max_by_len))

"""
https://education.yandex.ru/ege/inf/task/60136ef5-552a-4bc0-9224-2914e321d93b
"""

with open("24.txt") as f:
    s = f.readline().strip()
    for zn2 in "*-", "-*", "--", "**":
        s = s.replace(zn2, " ")

    for digit in '0123456789':
        s = s.replace("*0" + digit, "*0 " + digit)

    s = s.split()

    for i in range(len(s)):
        s[i] = s[i].lstrip("*-")

    s.sort(key=len, reverse=True)
    print(len(s[0]))
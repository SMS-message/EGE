"""
https://inf-ege.sdamgia.ru/problem?id=16815
"""

def b(n: int | str):
    return f"{int(n):08b}"

print(*(b(i) for i in "98.162.71.94".split(".")))
print(*(b(i) for i in "98.162.71.64".split(".")))

print(int("1000000", 2))
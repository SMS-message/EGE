"""
https://inf-ege.sdamgia.ru/problem?id=3541
"""

print(*map(lambda x: f"{int(x):08b}", "255.255.248.0".split(".")))
print(int("100000000000", 2) - 2)
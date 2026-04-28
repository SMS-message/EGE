"""
https://inf-ege.sdamgia.ru/problem?id=2236
"""

print(*map(lambda x: f"{int(x):08b}", "255.255.254.0".split(".")))
print(int("1000000000", 2) - 2)
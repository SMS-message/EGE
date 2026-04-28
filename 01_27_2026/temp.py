"""
№23808 (Уровень: Средний)
"""

from itertools import product, permutations

REPEAT: int = 7
STRING: str = "НЕАТОК"

p = set(permutations(sorted("КОТЕНОК"), r=7))
variants = tuple(product(sorted(STRING), repeat=REPEAT))
for i, variant in tuple(enumerate(variants, 1))[::-1]:
    if i % 2:
        if variant in p:
            print(i, variant)
            break

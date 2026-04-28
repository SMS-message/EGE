from itertools import product

a = tuple(product(sorted("БЛОГЕР"), repeat=4))

c = 0

vow = "ОЕ"

for word in a:
    if word.count("Г") == 1:
        is_valid = True
        is_vowel = False
        for sym in word:
            if is_vowel:
                if sym in vow:
                    is_valid = False
                else:
                    is_vowel = False
            else:
                if sym in vow:
                    is_vowel = True
                else:
                    is_vowel = False

        if is_valid:
            c += 1

print(c)

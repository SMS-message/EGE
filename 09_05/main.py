from sys import stdin

inp = [i.split() for i in stdin]

for line in inp:
    dct = {}
    lst = []
    word = line[0]
    for letter in word:
        if letter in dct:
            dct[letter] += 1
        else:
            dct[letter] = 1

    for another_word in line[1:]:
        for letter in another_word:
            try:
                if another_word.count(letter) > dct[letter]:
                    break
            except KeyError:
                break
        else:
            lst.append(another_word)

    print(*sorted(lst, key=lambda x: -len(x)))

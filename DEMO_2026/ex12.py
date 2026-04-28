line = list("0" * 343 + "1" + "0" * 656)


for i, sym in enumerate(line):
    dct = {
        "1": lambda x: "0" and quit(0),
        "0": "1",
    }
    line[i] = dct[sym]

print(line.count("0"))

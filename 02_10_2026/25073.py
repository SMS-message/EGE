"""
№ 25073 (Уровень: Базовый)
"""


MT = {
    "0*": "*R1",
    "1*": "*S1",
    "10": "1R1",
    "11": "0R1"
}

for number in range(70_000, -1, -1):
    bin_number = f"{number:b}"
    tape = list("*" * 5 + bin_number + "*" * 5)
    pos = 4
    state = "0"

    while True:
        cmd = MT[state + tape[pos]]
        tape[pos] = cmd[0]

        if cmd[1] == "S":
            break
        elif cmd[1] == "R":
            pos += 1
        else:
            cmd -= 1

        state = cmd[2]

    if int("".join(tape).strip("*"), 2) == 415:
        print(number)
        break

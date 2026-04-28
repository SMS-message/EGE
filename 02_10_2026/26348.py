"""
№ 26348 (Уровень: Базовый)
"""

MT = {
    "0*": "*R1",
    "1*": "1R2",
    "10": "1R1",
    "11": "0R1",
    "2*": "0R3",
    "3*": "*S3"
}

for number in range(1, 1000):
    bin_number = f"{number:b}"
    tape = list("*" * 5 + bin_number + "*" * 5)
    pos = 4
    state = "0"

    while True:
        cmd = MT[state + tape[pos]]
        tape[pos] = cmd[0]

        match cmd[1]:
            case "S":
                break
            case "L":
                pos -= 1
            case "R":
                pos += 1

        state = cmd[2]

    if int(''.join(tape).strip("*"), 2) == 794:
        print(number)
        break

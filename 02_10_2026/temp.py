"""
№ 25351 ЕГКР 13.12.25 (Уровень: Базовый)
"""

import typing

"""
Это модель машины Тьюринга, где ключ - состояние + текущий символ (Например, q1 - состояние (пишем без q)), 
а значение: на что поменять (символ), что далее сделать (S - стоп, R - направо, L - налево), в какое состояние перейти
"""

MT = {
    "0*": "*R1",
    "1*": "0R2",
    "10": "0R1",
    "11": "1R1",
    "2*": "0R3",
    "3*": "*S3"
}

number: int = 2028

bin_number: str = f"{number:b}"

tape: typing.MutableSequence[str] = list("*" * 5 + bin_number + "*" * 5)

position: int = 4
state: str = "0"

print(tape)

while True:
    cmd = MT[state + tape[position]]
    tape[position] = cmd[0]
    if cmd[1] == "S":
        break
    elif cmd[1] == "L":
        position -= 1
    else:
        position += 1
    state = cmd[2]

print(int(''.join(tape).strip("*"), 2))

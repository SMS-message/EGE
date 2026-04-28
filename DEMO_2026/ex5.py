def get_r(n: int):
    bin_n = f"{n:b}"
    r = bin_n + bin_n[-3:] if n % 3 == 0 else bin_n + f"{(n % 3) * 3:b}"

    return int(r, 2)


for i in range(100):
    r = get_r(i)
    if r >= 200:
        print(i, r)
        break

# Ответ: 26

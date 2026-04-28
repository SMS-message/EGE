def find_r(n: int):
    even_sum = sum(map(int, filter(lambda x: int(x) % 2 == 0, str(n))))
    even_ind_sum = sum(map(int, str(n)[::-1][::2]))
    return abs(even_sum - even_ind_sum)

assert find_r(4321) == 2

if __name__ == '__main__':
    i = 0
    while (r := find_r(i)) != 26:
        i += 1
    print(i, r)
def find_even_d(n: int):
    lst = [n] if n % 2 == 0 else []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                lst.append(i)
            if (i1 := n // i) % 2 == 0:
                lst.append(i1)
    return set(lst)

def check(n: int):
    if n % 2 == 0:
        if ((n // 2) ** 0.5).is_integer():
            return True
    return False

start = 1_850_000_000


k = 2
c = 0

while c < 5:
    if check(start + k):
        print(k, len(find_even_d(start + k)))
        c += 1
    k += 2

"""
№ 23765 Демоверсия 2026 (Уровень: Базовый)
"""

with open('26_23765.txt') as f:
    n = int(f.readline())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

all_products = []
do_not_count = []
top = []
bottom = []
last_i = 0

for i, datum in enumerate(data):
    ed1, ed2 = datum
    all_products.append([ed1, 1, i])
    all_products.append([ed2, 2, i])

all_products.sort()

for product in all_products:
    if product[-1] in do_not_count:
        continue
    if product[1] == 1:
        top.insert(0, product[-1])
    else:
        bottom.append(product[-1])
    do_not_count.append(product[-1])
    last_i = product[-1]

final_list = top + bottom[::-1]
print(last_i, len(final_list[final_list.index(last_i):]))

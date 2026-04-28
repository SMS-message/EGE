with open("DEMO_17.txt", mode="r") as file:
    count = 0

    lst = tuple(file.readlines())
    sum_lst = []
    int_lst = tuple(map(int, lst))

    min_2 = min(map(int, filter(lambda x: len(x.strip()) == 2, lst)))

    for i, elem1 in enumerate(int_lst):
        if i == len(int_lst) - 1:
            break
        elem2 = int_lst[i + 1]
        condition1 = ((len(str(elem1)) == 2) ^ (len(str(elem2)) == 2))
        condition2 = (sum((elem1, elem2)) % min_2 == 0)
        if condition1 and condition2:
            sum_lst.append(elem2 + elem1)
            count += 1

print(count)
print(max(sum_lst))

# Ответ: 150 9930

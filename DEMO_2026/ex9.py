from csv import reader

with open("DEMO_9.csv", mode="r", encoding="utf-8") as csvfile:
    a = reader(csvfile, delimiter=",", quotechar='"')
    for line in tuple(a)[::-1]:
        if len(set_line := set(line)) == 5:
            for num in line:
                if line.count(num) != 1:
                    found_num = num

            int_line = map(int, set_line - {found_num, })
            
            if sum(int_line) / len(set_line) <= int(found_num):
                print(line, sum(map(int, line)))
                break

# Ответ: 901

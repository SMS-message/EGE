"""
№ 19256 ЕГКР 21.12.24 (Уровень: Базовый)
"""

with open("26_19256.txt") as f:
    n = int(f.readline())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

tasks = {student: set() for student in map(lambda x: x[0], data)}
range_tasks = {i: 1 for i in map(lambda x: x[0], data)}

for student, task in data:
    tasks[student].add(task)

for student in tasks:
    c_max = 0
    c = 1
    s_task_student = sorted(tasks[student])
    for j, task in enumerate(s_task_student):
        if j + 1 == len(s_task_student):
            break
        if s_task_student[j + 1] - task == 1:
            c += 1
        else:
            c_max = max(c_max, c)
            c = 0
    range_tasks[student] = max(c_max, c)

print(*sorted(range_tasks.items(), key=lambda x: (-x[-1], x[0]))[0])

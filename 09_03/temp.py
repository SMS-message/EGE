def big_data(*data, key=lambda x: x[0]):
    lst = []
    for line in data:
        line_id, date, email = line
        day, month, year = date.split("-")
        username: str = email.split("@")[0]
        current_tuple = tuple((*line, username.lower().capitalize() + day[0] + month[-1] + year[-1]))
        lst.append(current_tuple)

    return list(sorted(lst, key=key))


if __name__ == '__main__':
    data = [(123, '14-05-2020', 'username@gmail.com'),
            (21, '12-06-2020', 'ara@gmail.com'),
            (4123, '02-09-2020', 'unknown@yandex.ru'),
            (1253, '17-05-2020', 'qwerty@mail.ru')]
    func = lambda x: x[-1]
    print(*big_data(*data, key=func), sep='\n')

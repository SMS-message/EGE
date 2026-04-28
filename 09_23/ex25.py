"""
Задание Комп. ЕГЭ №25 23282

Пусть М - сумма минимального и максимального простых натуральных делителей целого числа, не считая самого числа. Если таких делителей у числа нет, то значение М считается равным нулю.
Напишите программу, которая перебирает целые числа, большие 5 400 000, в порядке возрастания и ищет среди них такие, для которых М больше 60 000 и является палиндромом, т.е. одинаково читается слева направо и справа налево. В ответе запишите в первом столбце
таблицы первые  пять найденных чисел в порядке возрастания, а во втором столбце - соответствующие им значения М.
Например, для числа 298 M = 2 + 149 = 151.
Количество строк в таблице для ответа избыточно.
"""



def is_prime(n: int) -> bool:
    for delimiter in range(2, int(n ** 0.5) + 1):
        if n % delimiter == 0:
            return False
    return True


def is_palindrome(string: str):
    return string == string[::-1]


def find_delimiters(n: int):
    lst = []
    for delimiter in range(2, int(n ** 0.5) + 1):
        if n % delimiter == 0:
            lst.append(delimiter)
    return lst + [n // i for i in lst]


def find_m(n: int):
    delimiters = find_delimiters(n)
    min_del: int = 0
    max_del: int = 0
    for i in delimiters:
        if is_prime(i):
            min_del = i
    for i in delimiters[::-1]:
        if is_prime(i):
            max_del = i
    return min_del + max_del


assert find_m(298) == 151
assert is_palindrome("123321")
assert is_palindrome("12321")

if __name__ == '__main__':
    counter = 0
    x = 5_400_001
    while counter < 5:
        M = find_m(x)
        if M > 60_000 and is_palindrome(str(M)):
            print(x, M)
            counter += 1
        x += 1

"""
Ответ:

5400042 900009
5400420 90009
5400866 158851
5406116 1351531
5406420 90109
"""

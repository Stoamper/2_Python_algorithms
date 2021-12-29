'''
1.	Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
'''
import hashlib

def count_substring(user_string):
    substring_set = set()
    for i in range(len(user_string) + 1):
        for j in range(i + 1, len(user_string) + 1):
            substring_set.add(hashlib.sha1(user_string[i:j].encode('utf-8')).hexdigest())
            # print(substring_set)  # для тестового просмотра результатов
    return len(substring_set)

user_string = input('Введите строку, в которой хотите определить количество различных подстрок: ')
print(f'Количество различных подстрок в строке {user_string} равно {count_substring(user_string)}')





'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Исходная формулировка задачи:
5.1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
# На ПК 64-х разрядная ОС, версия Python 3.9
from sys import getsizeof

import collections

# Используем коллекцию defaultdict, так как в основе лежит словарь
dict_companies = collections.defaultdict(list)

sum = 0
sum_profit = 0
above_avrg = []
below_avrg = []

print(f'Первоначальный размер переменной dict_companies типа {type(dict_companies)} составляет {getsizeof(dict_companies)} байтов')
print(f'Первоначальный размер переменной sum типа {type(sum)} составляет {getsizeof(sum)} байтов')
print(f'Первоначальный размер переменной sum_profit типа {type(sum_profit)} составляет {getsizeof(sum_profit)} байтов')
print(f'Первоначальный размер переменной above_avrg типа {type(above_avrg)} составляет {getsizeof(above_avrg)} байтов')
print(f'Первоначальный размер переменной below_avrg типа {type(below_avrg)} составляет {getsizeof(below_avrg)} байтов\n')

# Указываем количество предприятий и заполняем словарь информацией по ним
n = int(input('Введите количество предприятий: '))
for i in range(n):
    company_name = input(f'Введите имя {i + 1}-й компании: ')
    # profit_quaters = []
    sum_profit = 0
    for j in range(4):
        profit = int(input(f'Введите прибыль {company_name} за {j + 1} квартал: '))
        sum_profit += profit
        sum += profit
    dict_companies[company_name] = sum_profit

# Вычисляем среднее значение годовой прибыли
avrg_year_profit = int(sum / n)

# Ищем предприятия со значением годовой прибыли больше или меньше средней
for key, val in dict_companies.items():
    if val > avrg_year_profit:
        above_avrg.append(key)
    else:
        below_avrg.append(key)

print(f'Компании, у которых годовая прибыль выше средней {avrg_year_profit}: ', above_avrg)
print(f'Компании, у которых годовая прибыль ниже средней {avrg_year_profit}: ', below_avrg)

print(f'\nРазмер переменной n типа {type(n)} после работы программы составляет {getsizeof(n)} байтов')
print(f'Размер переменной dict_companies типа {type(dict_companies)} после работы программы составляет {getsizeof(dict_companies)} байтов')
print(f'Размер переменной sum типа {type(sum)} после работы программы составляет {getsizeof(sum)} байтов')
print(f'Размер переменной sum_profit типа {type(sum_profit)} после работы программы составляет {getsizeof(sum_profit)} байтов')
print(f'Размер переменной above_avrg типа {type(above_avrg)} после работы программы составляет {getsizeof(above_avrg)} байтов')
print(f'Размер переменной below_avrg типа {type(below_avrg)} после работы программы составляет {getsizeof(below_avrg)} байтов')

'''
Первоначальные размеры переменных:
    1) dict_companies - 240 байтов (коллекция defaultdict)
    2) sum - 24 байтов (int)
    3) sum_profit - 24 байтов (int)
    4) above_avrg - 56 байтов (пустой список)
    5) below_avrg - 56 байтов (пустой список)
    
После работы программы размеры переменных изменились и приняли значения:
    1) dict_companies - 240 байтов (коллекция defaultdict)
    2) sum - 28 байтов (int)
    3) sum_profit - 28 байтов (int)
    4) above_avrg - 88 байтов (список)
    5) below_avrg - 88 байтов (список)
    6) n - 28 байтов (int)

Как видим, при сравнении программ без коллекций и с их использованием существенно отличается превоначальный
размер переменных dict_companies (пустой словарь - 64 байтов, коллекция - 240 байтов)

Окончательные размеры этих переменных отличаются не так сильно (словарь - 232 байтов, коллекция 240 байтов).
Эффективнее память используется в программе без коллекций с использованием словаря.
'''
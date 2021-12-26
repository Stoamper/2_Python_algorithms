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

dict_companies = {}
sum_profit = 0
above_avrg = {}
below_avrg = {}

print(f'Первоначальный размер переменной dict_companies типа {type(dict_companies)} составляет {getsizeof(dict_companies)} байтов')
print(f'Первоначальный размер переменной sum_profit типа {type(sum_profit)} составляет {getsizeof(sum_profit)} байтов')
print(f'Первоначальный размер переменной above_avrg типа {type(above_avrg)} составляет {getsizeof(above_avrg)} байтов')
print(f'Первоначальный размер переменной below_avrg типа {type(below_avrg)} составляет {getsizeof(below_avrg)} байтов\n')


n = int(input('Введите количество предприятий: '))
for i in range(n):
    company_name = input(f'Введите имя {i + 1}-й компании: ')
    profit_quaters = []
    print(f'Первоначальный размер переменной profit_quaters типа {type(profit_quaters)} составляет {getsizeof(profit_quaters)} байтов\n')
    for j in range(4):
        profit = int(input(f'Введите прибыль {company_name} за {j + 1} квартал: '))
        profit_quaters.append(profit)
        sum_profit += profit
    dict_companies[company_name] = profit_quaters
    # profit_quaters = None # описание приведено в конце


avrg_year_profit = int(sum_profit / n)

for key, val in dict_companies.items():
    if sum(val) >= avrg_year_profit:
        above_avrg[key] = sum(val)
    else:
        below_avrg[key] = sum(val)

print(f'Компании, у которых годовая прибыль выше средней {avrg_year_profit}: ', above_avrg)
print(f'Компании, у которых годовая прибыль ниже средней {avrg_year_profit}: ', below_avrg)

print(f'\nРазмер переменной n типа {type(n)} после работы программы составляет {getsizeof(n)} байтов')
print(f'Размер переменной dict_companies типа {type(dict_companies)} после работы программы составляет {getsizeof(dict_companies)} байтов')
print(f'Размер переменной sum_profit типа {type(sum_profit)} после работы программы составляет {getsizeof(sum_profit)} байтов')
print(f'Размер переменной above_avrg типа {type(above_avrg)} после работы программы составляет {getsizeof(above_avrg)} байтов')
print(f'Размер переменной below_avrg типа {type(below_avrg)} после работы программы составляет {getsizeof(below_avrg)} байтов')
print(f'Размер переменной profit_quaters типа {type(profit_quaters)} после работы программы составляет {getsizeof(profit_quaters)} байтов')

'''
Первоначальные размеры переменных:
    1) dict_companies - 64 байтов (пустой словарь)
    2) sum_profit - 24 байтов (int)
    3) above_avrg - 64 байтов (пустой словарь)
    4) below_avrg - 64 байтов (пустой словарь)
    5) profit_quaters - 56 байтов (пустой список)
    
После работы программы размеры переменных изменились и приняли значения:
    1) dict_companies - 232 байтов (словарь)
    2) sum_profit - 28 байтов (int)
    3) above_avrg - 232 байтов (словарь)
    4) below_avrg - 232 байтов (словарь)
    5) profit_quaters - 88 байтов (список)
    6) n - 28 байтов (int)

Переменная profit_quaters выходит из цикла ввода информации по предприятиям со значением.
Возможность для улучшения: в конце цикла присвоить переменной profit_quaters значение None.
Фрагмент кода:
...
    dict_companies[company_name] = profit_quaters
    profit_quaters = None
...
В таком случае ее окончательный размер вместо 88 байтов станет 16 байтов
'''





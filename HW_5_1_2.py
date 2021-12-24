'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
import collections

# Используем коллекцию defaultdict, так как в основе лежит словарь
dict_companies = collections.defaultdict(list)

sum = 0
sum_profit = 0
above_avrg = []
below_avrg = []

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


'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
dict_companies = {}
sum_profit = 0
above_avrg = {}
below_avrg = {}

n = int(input('Введите количество предприятий: '))
for i in range(n):
    company_name = input(f'Введите имя {i + 1}-й компании: ')
    profit_quaters = []
    for j in range(4):
        profit = int(input(f'Введите прибыль {company_name} за {j + 1} квартал: '))
        profit_quaters.append(profit)
        sum_profit += profit
    dict_companies[company_name] = profit_quaters


avrg_year_profit = int(sum_profit / n)
# print(dict_companies)
# print(avrg_year_profit)

for key, val in dict_companies.items():
    if sum(val) >= avrg_year_profit:
        above_avrg[key] = sum(val)
    else:
        below_avrg[key] = sum(val)

print(f'Компании, у которых годовая прибыль выше средней {avrg_year_profit}: ', above_avrg)
print(f'Компании, у которых годовая прибыль ниже средней {avrg_year_profit}: ', below_avrg)






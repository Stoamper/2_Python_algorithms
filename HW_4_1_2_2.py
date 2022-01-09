'''
6_1_2_2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
import timeit

setup_code = '''        # настройка кода 
even = 0    # счетчик четных цифр
odd = 0     # счетчик нечетных цифр

even_list = []  # список для внесения четных цифр
odd_list = []   # список для внесения нечетных цифр

number = int(input('Введите натуральное число: '))
'''

main_block = '''       # проверяемый блок
while number != 0:
    temp_num = number % 10
    number = number // 10
    if temp_num % 2 == 0:
        even += 1
        even_list.append(temp_num)
    else:
        odd += 1
        odd_list.append(temp_num)
    print(f'Количество четных цифр: {even}, в них вошли цифры {even_list}')
    print(f'Количество нечетных цифр: {odd}, в них вошли цифры {odd_list}')
'''

print(timeit.timeit(setup=setup_code, stmt=main_block, number=10))      # number - число повторений цикла

'''
Сложность алгоритма О(n) - линейная (так как выполняем поиск чисел в списке; 
чем больше список, тем дольше будет проводится поиск)

Оценка скорости работы алгоритма на рабочем ПК
Время выполнения алгоритма для трехзначного числа 123: 0.0001081959999997828 с
Время выполнения алгоритма для девятизначного числа 123123123: 0.00015566599999949915 с
Время выполнения алгоритма для восемнадцатизначного числа 123123123123123123: 0.00028652800000017464 с
'''







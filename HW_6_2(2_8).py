'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Исходная формулировка задачи:
2.8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''
# На ПК 64-х разрядная ОС, версия Python 3.9
from sys import getsizeof

repeat_quantity = 0

number = int(input('Введите число: '))
repeat_number = int(input('Введите число, количество повторов которого хотите посчитать: '))
initial_number = number

print(f'\nПервоначальный размер переменной repeat_quantity типа {type(repeat_quantity)} составляет {getsizeof(repeat_quantity)} байтов')
print(f'Первоначальный размер переменной number типа {type(number)} составляет {getsizeof(number)} байтов')
print(f'Размер переменной repeat_number типа {type(repeat_number)} составляет {getsizeof(repeat_number)} байтов')
print(f'Размер переменной initial_number типа {type(initial_number)} составляет {getsizeof(initial_number)} байтов\n')


while number != 0:
    temp_num = number % 10
    number = number // 10
    if temp_num == repeat_number:
        repeat_quantity += 1

print(f'Вы ввели число {initial_number}. Цифра {repeat_number} повторяется в нем {repeat_quantity} раз(а)\n')

print(f'Размер переменной temp_num типа {type(temp_num)} составляет {getsizeof(temp_num)} байтов')
print(f'Окончательный размер переменной repeat_quantity типа {type(repeat_quantity)} составляет {getsizeof(repeat_quantity)} байтов')
print(f'Окончательный размер переменной number типа {type(number)} составляет {getsizeof(number)} байтов')

'''
В результате работы программы видно, что первоначальный размер переменной repeat_quantity (int) был 24 байта.
После работы с переменной в цикле while ее размер вырос до 28 байт.
Первоначальный размер переменной number был 28 байт. 
После работы с переменной в цикле while ее размер уменьшился до 24 байт.

'''
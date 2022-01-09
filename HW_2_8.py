'''
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''

repeat_quantity = 0

number = int(input('Введите число: '))
repeat_number = int(input('Введите число, количество повторов которого хотите посчитать: '))
initial_number = number

while number != 0:
    temp_num = number % 10
    number = number // 10
    if temp_num == repeat_number:
        repeat_quantity += 1

print(f'Вы ввели число {initial_number}. Цифра {repeat_number} повторяется в нем {repeat_quantity} раз(а)')

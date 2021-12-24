'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
import collections

# Используем коллекцию deque, так как работаем со списком (библиотека не нужна в данном случае)
number_1_deque = collections.deque()
number_2_deque = collections.deque()

# Вводим значения в шестнадцатеричной системе счисления
print('Программа сложения и умножения двух шестнадцатеричных чисел')
number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')

# Добавляем введенные значения
number_1_deque.append(number_1)
number_2_deque.append(number_2)

# Определяем сумму чисел и их произведение
sum = hex(int(number_1_deque[0], base=16) + int(number_2_deque[0], base=16))
mult = hex(int(number_1_deque[0], base=16) * int(number_2_deque[0], base=16))
print(f'Сумма чисел {number_1} и {number_2} равна {sum[2:]}')
print(f'Произведение чисел {number_1} и {number_2} равно {mult[2:]}')

sum_deque = collections.deque(sum)
mult_deque = collections.deque(mult)
'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''

reverse_number = 0

number = int(input('Введите натуральное число: '))
initial_number = number

while number != 0:
    temp_num = number % 10
    number = number // 10
    reverse_number = str(reverse_number) + str(temp_num)

print(f'Для числа {int(initial_number)} обратное по порядку введенных чисел будет {int(reverse_number)}')
'''
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
'''

import random

rand_number = random.randint(0, 100)
try_quantity = 0

print('Компьютер загадал число')

while try_quantity < 10:
    user_number = int(input('Введите число от 0 до 100: '))
    if user_number < rand_number:
        try_quantity += 1
        print(f'Ваше число меньше загаданного. Осталось {10 - try_quantity} попыток')
    elif user_number > rand_number:
        try_quantity += 1
        print(f'Ваше число больше загаданного. Осталось {10 - try_quantity} попыток')
    else:
        print(f'Вы угадали (загадано число {rand_number}. Вы ввели {user_number})')
        break
else:
    print(f'Вы не угадали. Загаданное число {rand_number}')

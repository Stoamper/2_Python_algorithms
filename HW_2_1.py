'''
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
'''
symbol = None

print('Введите два числа и символ математической операции (+,-,*,/)', 'Для выхода введите 0 вместо символа', '', sep='\n')

while symbol != 0:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    symbol = input('Введите действие для указанных чисел: ')
    if symbol == '+':
        result = number_1 + number_2
        print(f'{number_1} + {number_2} =', result)
    elif symbol == '-':
        result = number_1 - number_2
        print(f'{number_1} - {number_2} =', result)
    elif symbol == '*':
        result = number_1 * number_2
        print(f'{number_1} * {number_2} =', result)
    elif symbol == '/':
        if number_2 == 0:
            print('Деление на 0 невозможно. Укажите второе число отличное от нуля')
        else:
            result = number_1 / number_2
            print(f'{number_1} / {number_2} =', result)
    elif symbol == '0':
        print('Завершение работы программы')
        break
    else:
        print('Указан неверный символ действия с числами. Введите заново')
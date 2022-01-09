'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''
numbers = []
sum_numbers = []
user_number = None

def sum_of_numbers(numbers):
    for i in range(len(numbers)):
        sum_number = 0
        number = numbers[i]
        # print(number)
        while number != 0:
            temp_num = number % 10
            number = number // 10
            sum_number = sum_number + temp_num
        sum_numbers.append(sum_number)
    return sum_numbers

def max_sum(sum_numbers, numbers):
    max_sum = sum_numbers[0]
    for i in range(len(sum_numbers)):
        if max_sum < sum_numbers[i]:
            max_sum = sum_numbers[i]
            number = numbers[i]
    print(f'Наибольшая сумма цифр {max_sum} выявлена у числа {number}')



while user_number != '+':
    user_number = input('Введите целое число (для выхода введите +): ')
    if user_number == '+':
        break
    numbers.append(int(user_number))

max_sum(sum_of_numbers(numbers), numbers)


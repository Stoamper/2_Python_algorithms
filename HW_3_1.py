'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''
multiple_numbers = 0

for i in range(2, 100):
    # print(i)
    for j in range(2, 10):
        if i % j == 0:
            multiple_numbers += 1

print(f'Количество чисел, кратных каждому из чисел в диапазоне от 2 до 9 равно {multiple_numbers}')
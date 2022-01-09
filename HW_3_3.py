'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint

rand_arr = []

# Создание массива случайных чисел
for i in range(10):
    rand_arr.append(randint(0, 100))

# Определение минимального и максимального элементов массива
min_elem = rand_arr[0]
max_elem = rand_arr[0]

for i in range(len(rand_arr)):
    if rand_arr[i] > max_elem:
        max_elem = rand_arr[i]
        i_max = i
    if rand_arr[i] < min_elem:
        min_elem = rand_arr[i]
        i_min = i

print(f'Изначальный массив имеет вид: {rand_arr}')
print(f'Максимальный элемент: {max_elem}, его номер {i_max}')
print(f'Минимальный элемент: {min_elem}, его номер {i_min}')

# Смена местами максимального и минимального элемента
rand_arr[i_max] = min_elem
rand_arr[i_min] = max_elem

print(f'Массив после смены местами максимального и минимального элементов: {rand_arr}')


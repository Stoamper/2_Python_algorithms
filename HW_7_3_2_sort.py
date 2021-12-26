'''
3.	Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках.

ВАРИАНТ С ПРЕДВАРИТЕЛЬНОЙ СОРТИРОВКОЙ
'''
import random
import math

rand_arr = []

def shell_sort_median(user_arr):
    n = len(user_arr)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = user_arr[i]
            j = i
            while j >= interval and user_arr[j - interval] > temp:
                user_arr[j] = user_arr[j - interval]
                j -= interval
            user_arr[j] = temp
        k -= 1
        interval = 2 ** k - 1
    print(f'Отсортированный по методу Шелла массив: {user_arr}')
    print(f'Медиана массива: {user_arr[len(user_arr) // 2]}')

m = int(input('Введите число m для определения размера массива по формуле 2m+1: '))
for i in range(2 * m + 1):
    rand_arr.append(random.randint(0, 100))

print(f'Первоначальный вид массива: {rand_arr}')
shell_sort_median(rand_arr)
'''
1.	Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''
import random

rand_arr = []
test_arr = [1, 2, 3, 4, 5]

for i in range(10):
    rand_arr.append(random.randint(-100, 99))

print(rand_arr)

def bubble_sort(user_arr):
    n = 1
    if len(user_arr) == 1:
        return user_arr
    else:
        while n < len(user_arr):
            for i in range(len(user_arr) - n):
                if user_arr[i] > user_arr[i+1]:
                    user_arr[i], user_arr[i+1] = user_arr[i+1], user_arr[i]
            n += 1
        return user_arr

# print(bubble_sort(rand_arr))
print(bubble_sort(test_arr))
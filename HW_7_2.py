'''
2.	Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''
import random

rand_arr = []
# test_arr = [1, 2, 3, 4]

for i in range(10):
    rand_arr.append(round((random.random() * 50), 2))

print(rand_arr)

def merge_sort(user_arr):
    if len(user_arr) <= 1:
        return user_arr
    mid = len(user_arr) // 2
    left = merge_sort(user_arr[:mid])
    right = merge_sort(user_arr[mid:])
    return merge(left, right, user_arr.copy())

def merge(left, right, merged_arr):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged_arr[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged_arr[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged_arr[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged_arr[left_cursor + right_cursor] = right[right_cursor]

    return merged_arr

print(merge_sort(rand_arr))
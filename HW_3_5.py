'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''

user_arr = [-11, -5, -1, -33, -44, -100]  # Пользовательский массив
min_number = user_arr[0]

for i in range(len(user_arr)):
    if user_arr[i] < min_number:
        min_number = user_arr[i]
        i_min = i

print(f'Максимальный отрицательный элемент имеет значение {min_number}, его номер в массиве {i_min}')
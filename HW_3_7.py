'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

user_arr = [11, 55, 5, 33, 44, -1, 42]  # Пользовательский массив
min_number_1 = user_arr[0]
min_number_2 = user_arr[0]

# Нахождение самого минимального числа
for i in range(len(user_arr)):
    if user_arr[i] < min_number_1:
        min_number_1 = user_arr[i]
        i_min_1 = i

user_arr.remove(min_number_1)

# Нахождение числа больше/равного минимальному и меньше всех остальных
for i in range(len(user_arr)):
    if user_arr[i] < min_number_2 and min_number_2 >= min_number_1:
        min_number_2 = user_arr[i]
        i_min_2 = i

# Вывод итоговой информации (если числа разные или они равны)
if min_number_1 != min_number_2:
    print(f'Самое минимальное число {min_number_1}')
    print(f'Второе минимальное число {min_number_2}')
elif min_number_1 == min_number_2:
    print(f'Оба минимальных числа равны между собой и равны {min_number_1}')
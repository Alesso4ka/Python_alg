#Задание 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import randint

def median_without_sort(arr):
    pivot = arr[0]

    less_med_elems = []
    greater_med_elems = []
    left_med_shoulder = 0
    right_med_shoulder = 0

    for i in array:
        if i < pivot:
            left_med_shoulder += 1
        elif i > pivot:
            right_med_shoulder += 1

        if i in arr:
            if i < pivot:
                less_med_elems.append(i)
            elif i > pivot:
                greater_med_elems.append(i)

    if left_med_shoulder > right_med_shoulder:
        return median_without_sort(less_med_elems)
    elif left_med_shoulder < right_med_shoulder:
        return median_without_sort(greater_med_elems)

    return pivot


n = int(input('Please enter a positive integer: '))
m = 2 * n + 1
print(f'Amount of elements m = 2 * {n} + 1 = {m}')

max_val = pow(m, 2)
array = []
while len(array) < m:
    x = randint(0, max_val)
    if x not in array:
        array.append(x)

print(f'Median for array {array} of {m} elements = {median_without_sort (array)} without sorting')

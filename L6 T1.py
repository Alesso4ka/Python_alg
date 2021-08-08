# Задание №1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
#Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

'''lesson-03_7'''
import random
import sys

r = [random.randint(0, 99) for _ in range(100)]
print(f'Array: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'The two smallest elements: {r[min_index_1]} и {r[min_index_2]}')

print('Sheet size', sys.getsizeof(r))
print('Sheet element size', sys.getsizeof(r[0]))
print('Tuple size', sys.getsizeof(tuple(r)))
print('Tuple element size', sys.getsizeof(tuple(r)[0]))
sum = 0
for size in r:
    sum += sys.getsizeof(size)
print('The size of all elements in the sheet', sum)

#Размер листа больше, чем неизменяемый кортеж, с одним набором данных
#(904 байт у листа 840 байт у кортежа). Размер не зависит от разрядности чисел.
#Зависит от размера массива.
#Каждый элемент массива занимает 28 байт. 100 элементов по 28 байт занимают
#2800 байт. Это значительно больше размера массива этих данных, т.к. Python
#делает оптимизацию и создаёт ссылки на один и тот же объект.

#Python 3.8 64-bit
#Задание 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

r = [random.randint(-99, 99) for _ in range(100)]
print(f'Array: {r}')

min_index = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)

if r[min_index] >= 0:
    print(f'There are no negative elements in the array')
else:
    print(f'In an array, the minimum negative element is: {r[min_index]}.',
            f'Located in the array at position {min_index}')

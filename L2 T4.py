#Задание 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#Количество элементов (n) вводится с клавиатуры.

n = int(input('Enter the number of items: '))
i = 0
range_number = 1
sum = 0
while i < n:
    sum += range_number
    range_number /= -2
    i += 1

print(f'Sum {sum}')

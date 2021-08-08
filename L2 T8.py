#Задание 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
#Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

user_range = input('Enter a sequence of numbers separated by a space: ')
user_patten = input('Enter the number to search for: ')
count = 0

for i in user_range:
    if i == user_patten:
        count += 1

print(
    f'The digit occurs {user_patten} in the sequence {user_range}: \
{count} times'
        )

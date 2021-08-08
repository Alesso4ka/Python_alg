#Задание 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#Вывести на экран это число и сумму его цифр.'''

def sum_numbers(number):
    sum = 0
    for f in number:
        sum += int(f)
    return sum


list_number = [i for i in input('Enter natural numbers separated by a space and press Enter').split()]

max_number = 0
max_sum = 0
for i in list_number:
    if sum_numbers(i) > max_sum:
        max_number = i
        max_sum = sum_numbers(i)

print(f'The number {max_number} had the largest sum of digits - {max_sum}')

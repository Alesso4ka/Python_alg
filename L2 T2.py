#Задание 2. Посчитать четные и нечетные цифры введенного натурального числа.
#Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Enter your number: ')
even = 0
odd = 0
for f in number:
    i = int(f)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Number {number} have: even digits - {even}, odd - {odd} ')

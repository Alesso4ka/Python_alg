# Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например,
# если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

def randchar(a, b):
    return chr(random.randint(ord(a), ord(b))) if a < b else chr(random.randint(ord(b), ord(a)))

def randint(a, b):
    return random.randint(a, b) if a < b else random.randint(b, a)

def randuni(a, b):
    return random.uniform(a, b) if a < b else random.uniform(b, a)

def bounds(str):
    num_list = str.split(',')
    a = int(num_list[0])
    b = int(num_list[1])
    return a, b

choise = int(input('Enter action number\n'
                   '1. Outputting a random integer\n'
                   '2. Outputting a random real number\n'
                   '3. Random character output\n'))
if choise != 1 and choise != 2 and choise != 3:
    exit('Invalid action number entered')

if choise == 1:
    d1 = input('Enter a range for a random integer (2 digits separated by commas)')
    a, b = bounds(d1)
    print(randint(a, b))

if choise == 2:
    d1 = input('Enter a range for a random real number (2 digits separated by commas)')
    a, b = bounds(d1)
    print(randuni(a, b))

if choise == 3:
    d1 = input('Enter a range for a random letter (2 letters separated by commas)')
    char_list = d1.split(',')
    a = char_list[0]
    b = char_list[1]
    print(randchar(a, b))

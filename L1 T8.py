# Задание 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('enter the year to determine if it is a leap year: '))

if year % 4 != 0:
    print('This is not a leap year')
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print('This is a leap year')
        else:
            print('This is not a leap year')
    else:
        print('This is a leap year')

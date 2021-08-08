# Задание 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Enter your number: ')

sum = 0
prod = 1

for f in number:
    sum += int(f)
    prod *= int(f)
print(f"The sum of the digits of a three-digit number {number} is {sum}")
print(f"The product of the digits of a three-digit number {number} is {prod}")

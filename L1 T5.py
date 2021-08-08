# Задание 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят
# и сколько между ними находится букв.

letter1, letter2 = [
  x.upper() for x in input('Enter two letters, separated by a space (A - Z): ').split()
]

# Generating a list of letters
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

index_letter1 = abc_list.index(letter1) + 1
index_letter2 = abc_list.index(letter2) + 1

if index_letter1 < index_letter2:
    step = 1
else:
    step = -1

print(f'The first letter, {letter1}, is in position: {index_letter1}')
print(f'The second letter, {letter2}, is in position: {index_letter2}')

print(
    f'There are letters in between \
{abc_list[abc_list.index(letter1) + step:abc_list.index(letter2):step]} \
({abs(index_letter1 - index_letter2) - 1})'
        )

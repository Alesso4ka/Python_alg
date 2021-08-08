# Задание 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

abc_number = int(input('Enter the letter number in the alphabet: '))

# Generating a list of letters
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if abc_number <= len(abc_list):
    print(f'Letter under the number {abc_number}: {abc_list[abc_number - 1]}')
else:
    print(
      f'Number entered in excess of the number of letters in the alphabet ({len(abc_list)})'
    )

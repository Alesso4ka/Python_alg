#Задание5. Вывести на экран коды и символы таблицы ASCII,
#начиная с символа под номером 32 и заканчивая 127-м включительно.
#Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

i = 1
for char in range(32, 128):
    if i % 10 == 0:
        print(f'{char:5}: {chr(char)}')
    else:
        print(f'{char:5}: {chr(char)}', end=' ')
    i += 1

# Задание 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

a = 5
b = 6
print('Given numbers {} и {}'.format(a, b))
print('Logical "AND": {}&{} = {}'.format(a, b, a & b))
print('Logical "OR": {}|{} = {}'.format(a, b, a | b))
print('Logical "EXCLUSIVE OR": {}^{} = {}'.format(a, b, a ^ b))
print('Logical "NEGATION": ~{} = {}'.format(a, ~a))
print('Shift to the left by two characters: {} << 2 = {}'.format(a, a<<2))
print('Shift to the right by two characters: {} >> 2 = {}'.format(a, a>>2))

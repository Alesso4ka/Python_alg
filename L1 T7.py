# Задание 7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a, b, c = [
      float(x) for x in input('Enter the lengths of the segments, separated by a space: ').split()
        ]

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print(f'Triangle with sides {a} {b} {c} - equilateral')
    elif a == b or b == c or c == a:
        print(f'Triangle with sides {a} {b} {c} - isosceles')
    else:
        print(f'Triangle with sides {a} {b} {c} - versatile')
else:
    print(f'Triangle with sides {a} {b} {c} does not exist')

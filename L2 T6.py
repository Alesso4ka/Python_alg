#6. В программе генерируется случайное целое число от 0 до 100.
#Пользователь должен его отгадать не более чем за 10 попыток.
#После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
#чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

from os import urandom as _urandom


def random_number():
    #The function generates a random number between 0 and 100.
    #The random number is returned by the _urandom function from the pseudo-random generator
    #operating system numbers. Bitwise shift to the right increases entropy.
    random = int(int.from_bytes(_urandom(7), 'big')) >> 5
    list = [n for n in range(0, 101)]
    return list[random % 100]


secret = random_number()
i = 1
while i <= 10:
    print(f'Attempt # {i: 2} of 10')
    user_number = int(input('Enter a number between 1 and 100: '))
    if user_number == secret:
        print('The guessed number is guessed ')
        break
    elif user_number > secret:
        print(f'Your number {user_number} is greater than the guess')
    else:
        print(f'Your number {user_number} is less than the guess')
    i += 1
if i > 10:
    print(f'Not guessed! The hidden number {secret}')

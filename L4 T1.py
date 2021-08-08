#Задание 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import math
import timeit


def sieve_without_eratosthenes(i):
    # Search function for the i-th prime,
    # without using the "Sieve of Eratosthenes" algorithm

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def sieve_eratosthenes(i):
    # Search function for the i-th prime,
    # using the "Sieve of Eratosthenes" algorithm

    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):
    # The function returns the upper boundary of the segment on which the
    # i-e is the number of prime numbers. The function is based on the theorem about
    # distribution of prime numbers, it states that the function
    # distribution of prime numbers. The number of prime numbers in a line segment
    # [1; n] grows with n as n / ln (n).

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

time1 = timeit.timeit(f'sieve_without_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import sieve_without_eratosthenes',
                      number=NUMBER_EXECUTIONS)

time2 = timeit.timeit(f'sieve_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import sieve_eratosthenes',
                      number=NUMBER_EXECUTIONS)

print(f'The program without using the "Sieve of Eratosthenes" algorithm is faster \
programs using the "Sieve of Eratosthenes" algorithm in \
{round (time2 / time1, 2)} times'
      )
# При запуске у меня: The program without using the "Sieve of Eratosthenes"
# algorithm is faster programs using the "Sieve of Eratosthenes" algorithm in 94.74 times

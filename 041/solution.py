#! encoding: utf8
from profile_decorate import profile
from pyprimes import isprime
from itertools import permutations


"""
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""


@profile
def main():
    greatest_prime = 0
    for n in range(9, 1, -1):
        digit_array = [str(i) for i in range(1, n + 1)]
        for number in permutations(digit_array, n):
            number = int(''.join(number))
            if isprime(number):
                if greatest_prime < number:
                    greatest_prime = number

        if greatest_prime > 0:
            print 'the largest n-digit prime is {}'.format(greatest_prime)
            break


if __name__ == '__main__':
    main()

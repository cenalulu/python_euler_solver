#! encoding: utf8
from profile_decorate import profile
from pyprimes import isprime
from itertools import count

"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""


@profile
def main():
    for i in count(3, 2):
        if not isprime(i):
            for j in count(1):
                twice_square = 2 * j * j
                if twice_square >= i:
                    print('we found a special number {}'.format(i))
                    return True
                else:
                    if isprime(i - twice_square):
                        break


if __name__ == '__main__':
    main()

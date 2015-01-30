#! encoding: utf8
from profile_decorate import profile
from itertools import count
from pyprimes import primes_below, isprime
from math import sqrt

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
"""

DISTINCT_COUNT = 4


@profile
def main():
    prime_list = [i for i in primes_below(1000)]
    consecutive = 0
    for i in count(1):
        factor_set = dict()
        remain_i = i

        if max(prime_list) == i:
            print max(prime_list)
            prime_list = [j for j in primes_below(i * 10)]

        if i in prime_list:
            consecutive = 0
            continue

        for prime in prime_list:
            while remain_i % prime == 0:
                factor_set[prime] = True
                remain_i = remain_i / prime
            if remain_i == 1:
                break

        if len(factor_set) == DISTINCT_COUNT:
            consecutive += 1
            if consecutive == DISTINCT_COUNT:
                print('we found 4 consecutvie numbers from {} to {}'.format(i - DISTINCT_COUNT + 1, i))
                break
        else:
            consecutive = 0


if __name__ == '__main__':
    main()

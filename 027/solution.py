#! encoding: utf8
from itertools import count
from prime import Prime
from profile_decorate import profile

"""Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

"""


@profile
def main():
    prime = Prime()
    prime_list = []
    prime_under_one_million = []
    for p in prime.get_prime():
        if p < 1000:
            prime_list.append(p)
            prime_under_one_million.append(p)
        elif p < 1000000:
            prime_under_one_million.append(p)
        else:
            break

    negative_prime_list = [0 - v for v in sorted(prime_list, reverse=True)]
    negative_prime_list.extend(prime_list)

    # b is try to be big, then n&b co efficient will be big
    # a is try to be small, then
    current_max_combination = 0
    for a in negative_prime_list:
        for b in negative_prime_list:
            combi_cnt = 0
            for n in count():
                if n * n + a * n + b not in prime_under_one_million:
                    break
                else:
                    combi_cnt += 1
            if combi_cnt > current_max_combination:
                print 'find an greater combination: a={}, b={} has {} combinations'.format(a, b, combi_cnt)
                current_max_combination = max(current_max_combination, combi_cnt)


if __name__ == '__main__':
    main()

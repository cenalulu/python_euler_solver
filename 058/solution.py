#! encoding: utf8
from profile_decorate import profile
from itertools import count
from pyprimes import isprime

"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?   j
"""


def prime_diagonal_cnt(level=None):
    diagonal_list = list()
    base_num = (2*level-1)**2
    for i in range(4):
        diagonal_list.append(base_num+2*level*(i+1))
    return diagonal_list


@profile
def main():
    prime_cnt = 0
    diagonal_cnt = 1
    for level in count(1):
        diagonal_cnt += 4
        for number in prime_diagonal_cnt(level):
            if isprime(number):
                prime_cnt += 1
        if diagonal_cnt > 10*prime_cnt:
            print(level*2+1)
            exit(0)


if __name__ == '__main__':
    main()

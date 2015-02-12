#! encoding: utf8
from profile_decorate import profile
from itertools import count

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""


class BaseValue:
    N = 101
    WATER_MARK = 1000000

    def __init__(self):
        self.N = 101


def cal_combinations(n=None, c=None):
    upper = 1
    down_left = 1
    down_right = 1
    if n and c:
        for i in range(1, n+1):
            upper *= i
        for i in range(1, c+1):
            down_left *= i
        for i in range(1, n-c+1):
            down_right *= i
    return upper/down_right/down_left


@profile
def main():
    result = 0
    for n in range(1, BaseValue.N):
        if n%2 == 0:
            if cal_combinations(n, n/2) < BaseValue.WATER_MARK:
                continue
            else:
                result += 1
                for c in range(n/2+1, n+1):
                    if cal_combinations(n, c) > BaseValue.WATER_MARK:
                        result += 1
                    else:
                        break
                for c in range(n/2-1, 0, -1):
                    if cal_combinations(n, c) > BaseValue.WATER_MARK:
                        result += 1
        else:
            if cal_combinations(n, (n-1)/2) < BaseValue.WATER_MARK \
                    and cal_combinations(n, (n+1)/2) < BaseValue.WATER_MARK:
                continue
            else:
                for c in range((n+1)/2, n+1):
                    if cal_combinations(n, c) > BaseValue.WATER_MARK:
                        result += 1
                    else:
                        break
                for c in range((n-1)/2, 0, -1):
                    if cal_combinations(n, c) > BaseValue.WATER_MARK:
                        result += 1
    print('total combination larger than one-million is {}'.format(result))


if __name__ == '__main__':
    main()

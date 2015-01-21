#! encoding: utf8
from profile_decorate import profile
from itertools import count

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def factorial(n=None):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def find_max_possible_len():
    for num_len in count(1):
        factorial_sum = factorial(9) * num_len
        if factorial_sum < (10 ** num_len - 1) / 9:
            return num_len


MAX_POSSIBLE = 10 ** (find_max_possible_len() - 1)


@profile
def main():
    factorial_cache = list()
    result_list = list()
    for digit in range(0, 10):
        factorial_cache.append(factorial(digit))

    for n in range(10, MAX_POSSIBLE):
        digit_factorial_sum = 0
        former_n = n
        while n > 0:
            digit = n % 10
            n = int(n / 10)
            digit_factorial_sum += factorial_cache[int(digit)]

        if digit_factorial_sum == former_n:
            print "curious number found: {}".format(former_n)
            result_list.append(former_n)

    print 'sum of all curious number is: {}'.format(sum(result_list))


if __name__ == '__main__':
    main()
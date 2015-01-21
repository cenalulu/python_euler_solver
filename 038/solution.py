#! encoding: utf8
from profile_decorate import profile
from itertools import count
from collections import defaultdict


"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_pandigital(n):
    digit_array = dict()
    for digit in list(n):
        if digit == '0':
            return False
        if digit in digit_array:
            return False
        else:
            digit_array[digit] = 0
    else:
        return True


@profile
def main():
    current_max_product = 1
    for base in range(1, 9999):
        str_now = ''
        for multiplier in count(1):
            str_now += str(base * multiplier)
            if len(str_now) >= 9:
                break
        if is_pandigital(str_now):
            current_max_product = max(current_max_product, int(str_now))

    print 'the max product of all pandigital concat str is {}'.format(current_max_product)


if __name__ == '__main__':
    main()

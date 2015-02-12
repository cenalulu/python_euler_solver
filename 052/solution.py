#! encoding: utf8
from profile_decorate import profile
from itertools import count

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
 but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def is_number_digit_equal(a=None, b=None):
    for digit in str(a):
        if digit not in str(b):
            return False
        elif str(a).count(digit) != str(b).count(digit):
            return False
    else:
        return True


@profile
def main():
    for i in count(1):
        for multiplier in [2, 3, 4, 5, 6]:
            if not is_number_digit_equal(i, multiplier*i):
                break
        else:
            print('we found the smallest int {}'.format(i))
            return


if __name__ == '__main__':
    main()

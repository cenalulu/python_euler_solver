from profile_decorate import profile
from itertools import count

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

POWER = 5
MAX_POSSIBLE_NUM = 1
for i in count(1):
    if 10 ** i > i * (9 ** POWER):
        MAX_POSSIBLE_NUM = i
        break

print 'the digit power is {}'.format(POWER)
print 'the max possible candidate is 10**{}'.format(MAX_POSSIBLE_NUM)


@profile
def main():
    sucess_list = list()
    for candidate in range(100, 10 ** MAX_POSSIBLE_NUM):
        str_len = len(str(candidate))
        digit_sum = 0
        level = 0
        for chars in str(candidate):
            digit_sum += int(chars) ** POWER

        if digit_sum == candidate:
            print 'number found: {}'.format(candidate)
            sucess_list.append(candidate)

    print 'sum of all requied numbers: {}'.format(sum(sucess_list))


if __name__ == '__main__':
    main()

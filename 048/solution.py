#! encoding: utf8
from profile_decorate import profile


"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""


@profile
def main():
    sum_now = 0
    for i in range(1, 1001):
        exp = i ** i
        sum_now += int(str(exp)[-10:])
    print('sum for 1000 number is {}'.format(str(sum_now)[-10:]))


if __name__ == '__main__':
    main()

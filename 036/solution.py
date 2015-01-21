#! encoding: utf8
from profile_decorate import profile

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def palidromic_num(upper_limit=None):
    current_value = 1
    if upper_limit:
        while current_value < upper_limit:
            if str(current_value) == str(current_value)[::-1]:
                yield current_value
            current_value += 1


def is_binary_palidromic(v_now):
    if str(bin(v_now))[2:] == str(bin(v_now))[2:][::-1]:
        return True
    else:
        return False


@profile
def main():
    UPPER_LIMIT = 1000000
    palindromic_sum = 0
    for i in palidromic_num(UPPER_LIMIT):
        if is_binary_palidromic(i):
            print "palindromic found {}".format(i)
            palindromic_sum += i

    print "sum of all palindromic in base 10 and 2 is {}".format(palindromic_sum)


if __name__ == '__main__':
    main()

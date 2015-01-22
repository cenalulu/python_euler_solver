#! encoding: utf8
from profile_decorate import profile
from itertools import count

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


def digit_generator():
    for n in count(1):
        for digit in list(str(n)):
            yield digit


@profile
def main():
    target_position_array = [1, 10, 100, 1000, 10000, 100000, 1000000]
    position = 1
    product_result = 1
    for digit in digit_generator():
        if position in target_position_array:
            product_result *= int(digit)
        position += 1
        if position > 1000000:
            break

    print 'product result is {}'.format(product_result)


if __name__ == '__main__':
    main()

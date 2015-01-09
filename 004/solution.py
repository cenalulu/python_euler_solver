#! encoding: utf8
import itertools

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindromic(v=0):
    v = str(v)
    for i in range(0, int(len(v) / 2)):
        if v[i:i + 1] != v[len(v) - 1 - i:len(v) - i]:
            return False
    else:
        return int(v)


biggest_pal = 0
number_tuple = [i for i in range(100, 1000)]
for base_v in number_tuple:
    for mult_v in number_tuple:
        mul_result = is_palindromic(int(base_v) * int(mult_v))
        if mul_result:
            if biggest_pal < mul_result:
                biggest_pal = mul_result
                pal_tuple = (base_v, mult_v)

print biggest_pal
print pal_tuple

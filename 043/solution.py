#! encoding: utf8
from profile_decorate import profile
from itertools import permutations

"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""


@profile
def main():
    divisor_array = [2, 3, 5, 7, 11, 13, 17]
    digit_array = [str(i) for i in range(10)]
    total_sum = 0
    for number_to_test in permutations(digit_array, 10):
        for pos in range(7):
            if not int(''.join(number_to_test[pos + 1:pos + 4])) % divisor_array[pos] == 0:
                break
        else:
            total_sum += int(''.join(number_to_test))
            print('curious pandigital found {}'.format(number_to_test))
    print('total sum is {}'.format(total_sum))


if __name__ == '__main__':
    main()

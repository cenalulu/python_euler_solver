#! encoding: utf8
from profile_decorate import profile
from itertools import permutations

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
 for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
 multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be
written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

"""
1digit * 1digit != 8digit
log10(a)+log10(b) >= log10(c)
"""


@profile
def main():
    multiplicand_set = set()
    multiplier_set = set()
    result_set = set()
    total_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    pandigit_list = list()

    for multiplicand_cnt in range(1, 8):
        for multiplier_cnt in range(1, 9 - multiplicand_cnt + 1):
            if not max(multiplicand_cnt, multiplier_cnt) - 1 < 9 - (
                        multiplicand_cnt + multiplier_cnt) < multiplier_cnt + multiplicand_cnt:
                continue
            for multiplicand_set in permutations(total_set, multiplicand_cnt):
                multiplier_set = total_set - set(multiplicand_set)
                for multiplier_set in permutations(multiplier_set, multiplier_cnt):
                    result = int(''.join([str(d) for d in multiplicand_set])) \
                             * int(''.join([str(d) for d in multiplier_set]))
                    if set([int(d) for d in str(result)]) == total_set - set(multiplier_set) - set(multiplicand_set):
                        if len(str(result)) == len(set(total_set - set(multiplier_set) - set(multiplicand_set))):
                            pandigit_list.append(result)
    distinct_list = set(pandigit_list)
    print "sum of all pandigit number is {}".format(sum(distinct_list))


if __name__ == '__main__':
    main()
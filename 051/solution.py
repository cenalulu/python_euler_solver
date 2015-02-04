#! encoding: utf8
from profile_decorate import profile
from itertools import count, combinations
from pyprimes import isprime
import re

"""
By replacing the 1st digit of the 2-digit number *3,
 it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
 this 5-digit number is the first example having seven primes among the ten generated numbers,
  yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
   being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
 is part of an eight prime value family.
"""

FAMILY_CNT = 8


@profile
def main():
    for number in count(start=101, step=2):
        number = '0'+str(number)
        zero_digit_cnt = str(number).count('0')
        if zero_digit_cnt > 0:
            zero_digit_list = []
            for idx, c in enumerate(str(number)):
                if c == str('0'):
                    zero_digit_list.append(idx)
            for replace_cnt in range(1, zero_digit_cnt+1):
                for zero_idx_comb in combinations(zero_digit_list, replace_cnt):
                    non_family_cnt = 0
                    translated_num = number
                    for digit in range(0, 10):
                        for idx in zero_idx_comb:
                            translated_num = str(translated_num)[0:idx]+str(digit)+str(translated_num)[idx+1:]
                        # print('--- before {} after translated {}'.format(number,translated_num))
                        if not isprime(int(translated_num)):
                            non_family_cnt += 1
                            if non_family_cnt > 10-FAMILY_CNT:
                                break
                    if non_family_cnt == 10-FAMILY_CNT:
                        print('we found eight prime family {}'.format(number))
                        translated_num = number
                        for digit in range(0, 10):
                            for idx in zero_idx_comb:
                                translated_num = str(translated_num)[0:idx]+str(digit)+str(translated_num)[idx+1:]
                            if isprime(int(translated_num)):
                                print('the smallest prime of it is {}'.format(translated_num))
                                return


if __name__ == '__main__':
    main()

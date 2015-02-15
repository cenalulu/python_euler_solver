#! encoding: utf8
from profile_decorate import profile

"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
"""


def is_lychrel(n=None, non_lychrel_cache_list={0: False}):
    temp_sum = n
    for i in range(50):
        temp_sum = temp_sum+int(str(temp_sum)[::-1])
        if temp_sum not in non_lychrel_cache_list:
            if str(temp_sum) == str(temp_sum)[::-1]:
                non_lychrel_cache_list[n] = True
                return True
        else:
            return non_lychrel_cache_list[temp_sum]
    else:
        non_lychrel_cache_list[n] = False
        return False


@profile
def main():
    total_non_lychrel = 0
    for n in range(1, 10000):
        if not is_lychrel(n):
            total_non_lychrel += 1

    print('total {} non-lychrel'.format(total_non_lychrel))


if __name__ == '__main__':
    main()

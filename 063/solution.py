#! encoding: utf8
from profile_decorate import profile
from itertools import count


"""
The 5-digit number, 16807=75, is also a fifth power. Similarly,
the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def find_max_n():
    for n in count(1):
        if 10**(n-1) > 9**n:
            return n


@profile
def main():
    max_n = find_max_n()
    total_cnt = 0
    print("max possible power for n is {}".format(max_n))

    for n in range(1, max_n):
        for base in count(1):
            power = base**n
            if n == len(str(power)):
                print("we have {} as number {} {}th power".format(base**n, base, n))
                total_cnt += 1
            elif n < len(str(power)):
                break

    print("Answer: {}".format(total_cnt))


if __name__ == '__main__':
    main()

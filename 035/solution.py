#! encoding: utf8
from profile_decorate import profile
from prime import Prime
from itertools import permutations

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?


"""

TARGET = 1000000


@profile
def main():
    prime_ins = Prime()
    prime_hash = dict()
    circular_prime_list = list()
    for i in prime_ins.get_prime():
        if i < TARGET:
            prime_hash[i] = True
        else:
            break

    for prime in prime_hash:
        circular_list = []
        for i in range(1, len(str(prime))):
            circular_list.append(int(''.join(str(prime)[i:] + str(prime)[0:i])))
        for num in circular_list:
            if not num in prime_hash:
                break
        else:
            print "circular prime found: {}".format(prime)
            circular_prime_list.append(prime)

    print "count of all circular prime is {}".format(len(circular_prime_list))


if __name__ == '__main__':
    main()

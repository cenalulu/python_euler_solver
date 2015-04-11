#! encoding: utf8
from profile_decorate import profile
from pyprimes import primes, isprime
from itertools import combinations
from copy import copy

"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any
order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
 The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""


@profile
def main():
    prime_pair = dict()
    existing_set = dict()
    PAIR_COUNT = 5
    for single_prime in primes():
        # split prime into char combinations
        str_prime = str(single_prime)
        for break_pos in range(1, len(str_prime)):
            left = int(str_prime[:break_pos])
            right = int(str_prime[break_pos:])
            if left != 0 and right != 0 and isprime(left) and isprime(right) and left != right:
                if int(str(right)+str(left)) < single_prime:
                    continue
                if isprime(int(str(right)+str(left))):
                    # put this two prime pair into cache
                    # and left is definitely smaller than right
                    if left not in existing_set:
                        existing_set[left] = list()
                        existing_set[left].append(list({right}))
                    else:
                        for idx, single_set in enumerate(existing_set[left]):
                            for prime in single_set:
                                if not isprime(int(str(right)+str(prime))) or not isprime(int(str(prime)+str(right))):
                                    break
                            else:
                                existing_set[left][idx].append(right)
                                if len(existing_set[left][idx]) == PAIR_COUNT-1:
                                    existing_set[left][idx].append(left)
                                    return existing_set[left][idx]
                        existing_set[left].append(list({right}))

                    if right not in existing_set:
                        existing_set[right] = list()
                        existing_set[right].append(list({left}))
                    else:
                        for idx, single_set in enumerate(existing_set[right]):
                            for prime in single_set:
                                if not isprime(int(str(left)+str(prime))) or not isprime(int(str(prime)+str(left))):
                                    break
                            else:
                                existing_set[right][idx].append(left)
                                if len(existing_set[right][idx]) == PAIR_COUNT-1:
                                    existing_set[right][idx].append(right)
                                    return existing_set[right][idx]
                        existing_set[right].append(list({left}))


if __name__ == '__main__':
    result_set = main()
    print("sum of 5 prime is {}".format(sum(result_set)))


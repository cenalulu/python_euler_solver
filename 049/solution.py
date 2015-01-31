#! encoding: utf8
from profile_decorate import profile
from pyprimes import primes_below, isprime

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
 is unusual in two ways: (i) each of the three terms are prime, and,
  (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
 but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""


@profile
def main():
    biggest_prime_now = 10000
    while biggest_prime_now > 1000:
        biggest_prime_now = max(primes_below(biggest_prime_now - 1))
        for middle_prime in primes_below(biggest_prime_now - 1):
            if set(list(str(biggest_prime_now))) == set(list(str(middle_prime))):
                smallest_prime = 2 * middle_prime - biggest_prime_now
                if smallest_prime < 1000:
                    continue
                if isprime(smallest_prime):
                    if set(list(str(smallest_prime))) == set(list(str(middle_prime))):
                        print(
                        'we found a arithmetic seq {},{},{}'.format(smallest_prime, middle_prime, biggest_prime_now))


if __name__ == '__main__':
    main()

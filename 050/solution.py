#! encoding: utf8
from profile_decorate import profile
from pyprimes import primes_below, isprime
from itertools import count

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

UPPER_LIMIT = 1000000


@profile
def main():
    prime_list = list(primes_below(UPPER_LIMIT))
    prime_list_len = len(prime_list)
    consecutive_len = 0

    # find the longest possible len, which sum is below 1 million
    for consecutive_len in count(1):
        if sum(prime_list[:consecutive_len - 1]) > UPPER_LIMIT:
            break

    while consecutive_len > 0:
        i = 0
        sum_now = sum(prime_list[i:i + consecutive_len])

        while i + consecutive_len < prime_list_len:
            if sum_now > UPPER_LIMIT:
                break
            else:
                if isprime(sum_now):
                    print('found max consecutive primes sum {}'.format( \
                        sum_now \
                        ))
                    return
            sum_now = sum_now - prime_list[i] + prime_list[i + consecutive_len]
            i += 1
        consecutive_len -= 1


if __name__ == '__main__':
    main()

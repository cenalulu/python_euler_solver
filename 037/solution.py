#! encoding: utf8
from profile_decorate import profile
from prime import prime_list

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

# since we are told that there's only eleven truncatable primes
#so the max possible number length is 2+11-1 = 12
MAX_NUM_LEN = 12


@profile
def main():
    known_prime_list = [2, 3, 5, 7]
    known_truncatable_prime = list()

    for i in prime_list(start_from=10):
        if len(known_truncatable_prime) == 11:
            print 'sum of all truncatable primes is {}'.format(sum(known_truncatable_prime))
            break

        known_prime_list.append(i)
        digit_len = len(str(i))
        is_truncatable = True
        #from left to right
        for n in range(1, digit_len):
            if int(str(i)[n:]) not in known_prime_list:
                # print '{} is not truncatable because of {}'.format(i, int(str(i)[n:]))
                is_truncatable = False
                break
        if is_truncatable:
            for n in range(1, digit_len):
                if int(str(i)[0:n]) not in known_prime_list:
                    #print '{} is not truncatable because of {}'.format(i, int(str(i)[0:n]))
                    break
            else:
                print 'found truncatable prime {}'.format(i)
                known_truncatable_prime.append(i)


if __name__ == '__main__':
    main()

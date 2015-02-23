#! encoding: utf8
from profile_decorate import profile
from fractions import gcd


"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""


def get_nth_expansion(n=None):
    a = b = 1
    for repeat in range(n+1):
        (a, b) = (a+2*b, a+b)
        gcd_of_ab = gcd(a, b)
        (a, b) = (a/gcd_of_ab, b/gcd_of_ab)
        yield {'a': a, 'b': b}


@profile
def main():
    answer = 0
    for result in get_nth_expansion(1001):
        if len(str(result['a'])) > len(str(result['b'])):
            answer += 1
            # print('{} -- a:{a}, b:{b}'.format(i+1,**get_nth_expansion(i)))
    print('answer: {}'.format(answer))


if __name__ == '__main__':
    main()

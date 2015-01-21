#! encoding: utf8
from profile_decorate import profile
from fractions import gcd

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""


@profile
def main():
    product_of_nominator = 1
    product_of_denominator = 1
    for denominator in range(11, 100):
        for nominator in range(11, denominator):
            for digit in list(str(denominator)):
                if digit in list(str(nominator)) and digit != '0':
                    reduced_denominator_str = list(str(denominator))
                    reduced_nominator_str = list(str(nominator))
                    reduced_denominator_str.remove(digit)
                    reduced_nominator_str.remove(digit)
                    reduced_denominator = int(''.join(reduced_denominator_str))
                    reduced_nominator = int(''.join(reduced_nominator_str))
                    if reduced_denominator != 0:
                        if float(nominator) / denominator == float(str(reduced_nominator)) / int(
                                str(reduced_denominator)):
                            print 'found pair: nominator={}, denominator={}'.format(nominator, denominator)
                            product_of_nominator *= nominator
                            product_of_denominator *= denominator
    print "origin form:{}/{}".format(product_of_nominator, product_of_denominator)
    print "lowest common term:{}/{}".format(product_of_nominator / gcd(product_of_denominator, product_of_nominator),
                                            product_of_denominator / gcd(product_of_nominator, product_of_denominator))


if __name__ == '__main__':
    main()
#! encoding: utf8
from profile_decorate import profile

"""
Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""


def gen_100th_number():
    max_n = 100
    yield 2
    i = 1
    base = 2
    while True:
        yield 1
        i += 1
        if i == max_n:
            return

        yield base
        base += 2
        i += 1
        if i == max_n:
            return

        yield 1
        i += 1
        if i == max_n:
            return


@profile
def main():
    factor_list = [i for i in gen_100th_number()]
    factor_list.reverse()
    denominator = 1
    numerator = factor_list[0]
    factor_list = factor_list[1:]

    for n in factor_list:
        (denominator, numerator) = (numerator, denominator)
        numerator += n*denominator

    print("result is {}".format(sum([int(c) for c in list(str(numerator))])))


if __name__ == '__main__':
    main()

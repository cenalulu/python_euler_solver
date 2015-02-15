#! encoding: utf8
from profile_decorate import profile

"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""


@profile
def main():
    max_sum = 0
    for a in range(100):
        for b in range(100):
            max_sum = max(max_sum, sum(int(d) for d in str(a**b)))

    print("max sum of digits is {}".format(max_sum))


if __name__ == '__main__':
    main()

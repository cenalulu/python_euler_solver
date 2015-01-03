import sys

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

VALUE_SUM = 1000

for a in range(1, int(VALUE_SUM / 2)):
    for b in range(1, int((VALUE_SUM - a) / 2)):
        c = VALUE_SUM - a - b
        if a * a + b * b == c * c:
            print '{}'.format(a * b * c)
            sys.exit(0)


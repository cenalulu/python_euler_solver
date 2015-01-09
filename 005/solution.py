from itertools import count

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

opt_number_tuple = ( 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 )
for v in count(20):
    for i in opt_number_tuple:
        if v % i != 0:
            break
    else:
        print v
        break

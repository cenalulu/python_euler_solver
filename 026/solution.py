"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

nine_number = ''
cycle_divisor_list = []
for nine_len in range(1, 1000):
    nine_number += '9'
    nine_digit = int(nine_number)
    for i in range(1, 1000):
        if nine_digit % i == 0:
            for smaller_nine in range(1, nine_len):
                smaller_digit = '9' * smaller_nine
                if int(smaller_digit) % i == 0:
                    break
            else:
                cycle_divisor_list.append(i)
print cycle_divisor_list.pop()

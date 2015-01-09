#! encoding: utf8
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n) .
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""

divisor_sum_dict = {
    1: 0,
    2: 1
}
for i in range(1, 10000 + 1):
    divisor_sum = 1
    for divisor in range(2, i):
        if i % divisor == 0:
            divisor_sum += divisor

        divisor_sum_dict[i] = divisor_sum

amicable_pair_sum = 0
for idx, divisor_sum in divisor_sum_dict.items():
    if 10000 > divisor_sum > 1 and divisor_sum_dict[divisor_sum] == idx and divisor_sum != idx:
        amicable_pair_sum += idx

print amicable_pair_sum




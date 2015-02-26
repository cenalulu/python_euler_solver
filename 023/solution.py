"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
 though it is known that the greatest number that cannot be expressed as the sum of two abundant
 numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def is_abundant_number(num=0):
    divisor_sum = 1
    for divisor in range(2, num):
        if divisor * divisor > num:
            break
        else:
            if num % divisor == 0:
                divisor_sum += divisor + num / divisor
                if divisor * divisor == num:
                    divisor_sum -= divisor

    if divisor_sum > num:
        return True
    else:
        return False


def main():
    abundant_list = []
    for i in range(1, 28123):
        if is_abundant_number(i):
            abundant_list.append(i)

    print len(abundant_list)

    non_abund_sum_total = 0
    for num in range(1, 28123):
        for abundant_num in abundant_list:
            if abundant_num > num:
                continue
            else:
                if (num - abundant_num) in abundant_list:
                    break
        else:
            non_abund_sum_total += num
    print non_abund_sum_total


if __name__ == '__main__':
    main()


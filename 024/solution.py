"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""


def cal_factorial(n=0):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def main():
    digit_cnt = 10
    target_cnt = 1000000
    permutation_cnt_now = 0
    result_array = list()
    num_array = list(range(0, digit_cnt))
    for digit_position in range(0, digit_cnt):
        for candidate_value in sorted(num_array):
            print digit_position, candidate_value, permutation_cnt_now
            if permutation_cnt_now + cal_factorial(digit_cnt - digit_position - 1) > target_cnt - 1:
                num_array.remove(candidate_value)
                result_array.append(candidate_value)
                break
            else:
                permutation_cnt_now += cal_factorial(digit_cnt - digit_position - 1)

    result_value = [str(v) for v in result_array]
    print ''.join(result_value)


if __name__ == '__main__':
    main()

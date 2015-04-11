#! encoding: utf8
from profile_decorate import profile
from itertools import count

"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843)
and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly
three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def finger_print(number):
    fp_str = list()
    digit_profile = {digit: 0 for digit in range(0, 10)}
    for digit in list(str(number)):
        digit_profile[int(digit)] += 1

    for digit in range(0, 10):
        if digit_profile[digit] > 0:
            fp_str.append(str(digit)+str(digit_profile[digit]))

    return "_".join(fp_str)


@profile
def main():
    profile_dict = dict()
    current_digit_len = 1
    for base in count():
        cube = base**3
        fp = finger_print(cube)

        if len(str(cube)) > current_digit_len:
            current_digit_len += 1
            print("next level {}".format(current_digit_len))
            result_list = list()
            for fp in profile_dict:
                if len(profile_dict[fp]) == 5:
                    print("fp:{} is a candidate with elements {}".format(fp, profile_dict[fp]))
                    result_list.append(min(profile_dict[fp]))
            if len(result_list) > 0:
                print("result is {}".format(min(result_list)))
                return 0

            profile_dict = dict()

        if fp not in profile_dict:
            profile_dict[fp] = list()

        profile_dict[fp].append(cube)


if __name__ == '__main__':
    main()

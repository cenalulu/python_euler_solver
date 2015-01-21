#! encoding: utf8
from profile_decorate import profile

"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

COIN_ARRAY = [1, 2, 5, 10, 20, 50, 100, 200]
TOTAL_SUM = 200


@profile
def main():
    print cal_combination_count(TOTAL_SUM, COIN_ARRAY)


def cal_combination_count(remain_amount=0, coin_array=None):
    combination_cnt = 0
    element_coin = coin_array[0]
    if not coin_array:
        return 0
    if len(coin_array) == 0:
        return 0
    for repeat_times in range(0, int(remain_amount / element_coin) + 1):
        if remain_amount - repeat_times * element_coin == 0:
            combination_cnt += 1
        elif remain_amount - repeat_times * element_coin < 0:
            continue
        else:
            if len(coin_array) > 1:
                tmp_coin_array = coin_array[0:]
                tmp_coin_array.remove(element_coin)
                combination_cnt += cal_combination_count(remain_amount - element_coin * repeat_times, tmp_coin_array)

    return combination_cnt


if __name__ == '__main__':
    main()

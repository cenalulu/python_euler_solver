#! encoding: utf8
from profile_decorate import profile
from multiprocessing import Process, current_process, Value
from itertools import count

"""
"""


def is_abundant_number(num=0):
    divisor_sum = 1
    for divisor in range(2, num):
        if divisor*divisor > num:
            break
        else:
            if num%divisor == 0:
                divisor_sum += divisor+num/divisor
                if divisor*divisor == num:
                    divisor_sum -= divisor

    if divisor_sum > num:
        return True
    else:
        return False


def sum_of_redudant(start, step, end, abundant_list, partial_sum):
    result = 0
    sorted_list = sorted(abundant_list.keys())
    for i in range(start, end, step):
        is_find = False
        for abundant in sorted_list:
            if abundant*2 > i:
                break
            if abundant_list.has_key(i-abundant):
                is_find = True
                break

        if not is_find:
            result += i
    partial_sum.value += result


@profile
def main():
    # answer is 4179871
    process_list = list()
    # max_num = 28123
    max_num = 28124
    c = 4

    abundant_list = dict()
    for i in range(12, max_num):
        if is_abundant_number(i):
            abundant_list[i] = True

    result = Value('i', 0)

    for process_id in range(1, c+1):
        process = Process(name=str(process_id), target=sum_of_redudant,
                          kwargs={'start': process_id, 'step': c, 'end': max_num,
                                  'abundant_list': abundant_list, 'partial_sum': result})
        process.start()
        process_list.append(process)

    for p in process_list:
        p.join()
    print result.value


if __name__ == '__main__':
    main()

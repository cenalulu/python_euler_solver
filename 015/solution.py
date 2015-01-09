# encoding: utf8
import copy as copy

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

global_path_cache = {0: {0: 1}}


def cal_combinations_to_point(point=None):
    global global_path_cache
    row_cache = global_path_cache.get(point[0], None)
    if row_cache:
        path_cnt = row_cache.get(point[1], None)
        if path_cnt:
            return path_cnt
        else:
            if point[0] > 0 and point[1] > 0:
                global_path_cache[point[0]].setdefault(point[1], cal_combinations_to_point(
                    [point[0] - 1, point[1]]) + cal_combinations_to_point([point[0], point[1] - 1]))
                return global_path_cache[point[0]][point[1]]
            elif point[0] == 0 and point[1] > 0:
                global_path_cache[point[0]].setdefault(point[1], cal_combinations_to_point([point[0], point[1] - 1]))
                return global_path_cache[point[0]][point[1]]
            elif point[1] == 0 and point[0] > 0:
                global_path_cache[point[0]].setdefault(point[1], cal_combinations_to_point([point[0] - 1, point[1]]))
                return global_path_cache[point[0]][point[1]]
            else:
                return 1
    else:
        if point[0] > 0 and point[1] > 0:
            global_path_cache.update({point[0]: {
                point[1]: cal_combinations_to_point([point[0] - 1, point[1]]) + cal_combinations_to_point(
                    [point[0], point[1] - 1])}})
            return global_path_cache[point[0]][point[1]]
        elif point[0] == 0 and point[1] > 0:
            global_path_cache.update({point[0]: {point[1]: cal_combinations_to_point([point[0], point[1] - 1])}})
            return global_path_cache[point[0]][point[1]]
        elif point[1] == 0 and point[0] > 0:
            global_path_cache.update({point[0]: {point[1]: cal_combinations_to_point([point[0] - 1, point[1]])}})
            return global_path_cache[point[0]][point[1]]
        else:
            return 1


def cal_enumerations_path_count_of_matrix(matrix_size=0):
    return cal_combinations_to_point([matrix_size, matrix_size])


def main(*args, **kwargs):
    print cal_enumerations_path_count_of_matrix(20)


if __name__ == '__main__':
    main()

from profile_decorate import profile

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is
formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


class ClockwiseMatrix():
    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        self.current_level = 0
        self.current_value = 1
        self.matrix_xy = {0: {0: 1}}

    def __store_value(self, x, y, v):
        if x in self.matrix_xy:
            self.matrix_xy[x][y] = v
        else:
            self.matrix_xy[x] = dict()
            self.matrix_xy[x][y] = v

    def get_matrix(self, level=None):
        while True:
            self.current_value += 1
            if self.current_x == self.current_y and self.current_x >= 0:
                self.current_level += 1
                if self.current_level > level:
                    return self.matrix_xy
                self.current_x += 1
                self.__store_value(self.current_x, self.current_y, self.current_value)
                continue

            if self.current_y > -self.current_level and self.current_x == self.current_level:
                self.current_y -= 1
                self.__store_value(self.current_x, self.current_y, self.current_value)
                continue
            elif self.current_x > -self.current_level and self.current_y == -self.current_level:
                self.current_x -= 1
                self.__store_value(self.current_x, self.current_y, self.current_value)
                continue
            elif self.current_y < self.current_level and self.current_x == -self.current_level:
                self.current_y += 1
                self.__store_value(self.current_x, self.current_y, self.current_value)
                continue
            elif self.current_x < self.current_level:
                self.current_x += 1
                self.__store_value(self.current_x, self.current_y, self.current_value)
                continue
            else:
                raise Exception


@profile
def main():
    matrix_ins = ClockwiseMatrix()
    matrix_level = 500
    my_matrix = matrix_ins.get_matrix(matrix_level)
    diagonal_sum = 1
    for level in range(1, matrix_level + 1):
        diagonal_sum += my_matrix[level][level]
        diagonal_sum += my_matrix[-level][level]
        diagonal_sum += my_matrix[level][-level]
        diagonal_sum += my_matrix[-level][-level]

    print 'diagonal sum for a {level}x{level} matrix is: {sum}'.format(level=matrix_level, sum=diagonal_sum)


if __name__ == '__main__':
    main()

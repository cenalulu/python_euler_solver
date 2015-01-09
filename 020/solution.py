import operator

max = 100
print sum([int(digit) for digit in str(reduce(operator.mul, range(1, max + 1), 1))])